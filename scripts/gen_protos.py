#!/usr/bin/env python3
"""
Generate Python protobuf / gRPC stubs from the platform's contracts, zqnt-protos.

Source: PROTO_REF_COMMIT of a zqnt-protos clone, by default the sibling checkout ../zqnt-protos
(zqnt-platform/utils/zqnt-protos), or ZQNT_PROTOS_DIR. The files are read from that commit with
`git archive`, whatever the clone has checked out. zqnt-protos is private, so it is deliberately
not a submodule: uv clones a git dependency's submodules, and every consumer's CI would need
credentials for it.

zqnt-protos has four proto roots (see its README): public/{v2,v3} and internal/{v2,v3}. Only
internal/ is generated here:
  internal/v2  -> zqnt_utils/generated/zqnt/*_pb2.py
  internal/v3  -> zqnt_utils/generated/zqnt/<domain>/v3/*_pb2.py
public/ is on the include path only; its modules are those of zqnt-api (zqnt_api.generated...),
and imports of them are rewritten to that package, so no proto file is registered twice.

Pin: PROTO_REF_COMMIT. A commit without a release tag (a preview from a zqnt-protos PR branch) is
refused unless ALLOW_UNTAGGED=1. To move: set PROTO_REF_COMMIT, re-run, commit it together with the
regenerated code. Run with PYTHONDONTWRITEBYTECODE=1.

Usage:  python scripts/gen_protos.py
"""

import io
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

try:
    from grpc_tools import protoc
except ImportError:
    sys.exit("grpcio-tools is required: pip install grpcio-tools")

PROTO_REF_COMMIT = "490c23fc10f5949ce0721a927b995e273cda2c9d"

ROOT = Path(__file__).resolve().parent.parent
PROTOS_REPO = Path(os.environ.get("ZQNT_PROTOS_DIR", ROOT.parent / "zqnt-protos"))
GENERATED = ROOT / "zqnt_utils" / "generated"
V2_OUT = GENERATED / "zqnt"
PACKAGE_PREFIX = "zqnt_utils.generated."
PUBLIC_PREFIX = "zqnt_api.generated."

WELL_KNOWN_PROTOS = Path(protoc.__file__).parent / "_proto"


def _git(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(PROTOS_REPO), *args], capture_output=True, text=True
    )


def check_pin() -> None:
    """PROTO_REF_COMMIT must exist in the clone, and be a release unless explicitly a preview."""
    if not (PROTOS_REPO / ".git").exists():
        sys.exit(
            f"No zqnt-protos clone at {PROTOS_REPO} -- clone it there or set ZQNT_PROTOS_DIR"
        )
    if _git("cat-file", "-e", f"{PROTO_REF_COMMIT}^{{commit}}").returncode != 0:
        _git("fetch", "--quiet", "origin")
        if _git("cat-file", "-e", f"{PROTO_REF_COMMIT}^{{commit}}").returncode != 0:
            sys.exit(
                f"zqnt-protos {PROTO_REF_COMMIT} is not in {PROTOS_REPO}, not even after a fetch"
            )
    tag = _git("describe", "--tags", "--exact-match", PROTO_REF_COMMIT)
    if tag.returncode == 0:
        print(
            f"Generating from zqnt-protos {tag.stdout.strip()} ({PROTO_REF_COMMIT})..."
        )
    elif os.environ.get("ALLOW_UNTAGGED") == "1":
        print(
            f"Generating from untagged zqnt-protos {PROTO_REF_COMMIT} (preview, ALLOW_UNTAGGED=1)..."
        )
    else:
        sys.exit(
            f"zqnt-protos {PROTO_REF_COMMIT} carries no release tag. Pin a tag, or set ALLOW_UNTAGGED=1 "
            "for a preview from a zqnt-protos PR branch (it must move to the tag after the release)."
        )


def export_protos(target: Path) -> None:
    archive = subprocess.run(
        [
            "git",
            "-C",
            str(PROTOS_REPO),
            "archive",
            "--format=tar",
            PROTO_REF_COMMIT,
            "public/v2",
            "public/v3",
            "internal/v2",
            "internal/v3",
        ],
        check=True,
        capture_output=True,
    ).stdout
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        tar.extractall(target, filter="data")


def _protoc(proto_root: Path, public_root: Path, out: Path, files: list[Path]) -> None:
    args = [
        "grpc_tools.protoc",
        f"--proto_path={proto_root}",
        f"--proto_path={public_root}",
        f"--proto_path={WELL_KNOWN_PROTOS}",
        f"--python_out={out}",
        f"--pyi_out={out}",
        f"--grpc_python_out={out}",
        f"--mypy_grpc_out={out}",
        *[str(p) for p in files],
    ]
    rc = protoc.main(args)
    if rc != 0:
        sys.exit(f"protoc failed with exit code {rc}")


def ensure_init_files(directory: Path, stop: Path) -> None:
    """__init__.py in `directory` and every parent up to and including `stop`."""
    for dirpath in [directory, *directory.parents]:
        init = dirpath / "__init__.py"
        if not init.exists():
            init.write_text("")
        if dirpath == stop:
            break


def generate_v2(v2_dir: Path, public_v2: Path) -> None:
    files = sorted(v2_dir.glob("*.proto"))
    print(f"v2: {len(files)} proto file(s) -> {V2_OUT.relative_to(ROOT)}")
    V2_OUT.mkdir(parents=True, exist_ok=True)
    ensure_init_files(V2_OUT, GENERATED)
    _protoc(v2_dir, public_v2, V2_OUT, files)
    public = {f"{p.stem.replace('-', '_')}_pb2" for p in public_v2.glob("*.proto")}
    _fix_v2_imports(V2_OUT, public)


def generate_v3(v3_dir: Path, public_v3: Path) -> None:
    files = sorted(v3_dir.rglob("*.proto"))
    print(
        f"v3: {len(files)} proto file(s) -> {GENERATED.relative_to(ROOT)}/zqnt/<domain>/v3"
    )
    _protoc(v3_dir, public_v3, GENERATED, files)
    for proto in files:
        ensure_init_files(GENERATED / proto.relative_to(v3_dir).parent, GENERATED)
    public = {p.name for p in (public_v3 / "zqnt").iterdir() if p.is_dir()}
    _fix_v3_imports(GENERATED, public)


def _fix_v2_imports(directory: Path, public: set[str]) -> None:
    """
    grpc_tools emits absolute imports that only work if the output dir is on sys.path. Rewrite
    them so the package works when installed as zqnt_utils.generated.zqnt.*:

      `import simulator_control_pb2 as x`  ->  `from . import simulator_control_pb2 as x`
      `import common_pb2 as x`             ->  `from zqnt_api.generated.zqnt import common_pb2 as x`
      `from base_pb2 import *`             ->  `from zqnt_api.generated.zqnt.base_pb2 import *`

    The last form is emitted for `import public "base.proto";` (public re-exports).
    """
    bare_import = re.compile(r"^import (\w+_pb2) as (\w+)$", re.MULTILINE)
    star_import = re.compile(r"^from (\w+_pb2) import \*$", re.MULTILINE)

    def package(module: str) -> str:
        return f"{PUBLIC_PREFIX}zqnt" if module in public else ""

    for py_file in [*directory.glob("*.py"), *directory.glob("*.pyi")]:
        src = py_file.read_text()
        patched = bare_import.sub(
            lambda m: f"from {package(m[1]) or '.'} import {m[1]} as {m[2]}", src
        )
        patched = star_import.sub(
            lambda m: f"from {package(m[1])}.{m[1]} import *", patched
        )
        if patched != src:
            py_file.write_text(patched)


def _fix_v3_imports(directory: Path, public: set[str]) -> None:
    """
    v3 files import each other by package path (`from zqnt.capability.v3 import capability_pb2`).
    Internal domains get the zqnt_utils.generated. prefix, public ones zqnt_api.generated. In .py
    files only the import lines and the module name handed to the descriptor builder are touched;
    the serialized descriptor itself also contains "zqnt.capability.v3" and must stay byte-exact.
    The .pyi stubs carry no descriptor, so their type references are rewritten throughout.
    """
    v3_module = r"zqnt\.[a-z_]+\.v3"
    py_import = re.compile(rf"^(from|import) ({v3_module})", re.MULTILINE)
    builder = re.compile(
        rf"(BuildTopDescriptorsAndMessages\(DESCRIPTOR, ')({v3_module})"
    )
    pyi_ref = re.compile(rf"(?<![\w.])({v3_module})")

    def prefixed(module: str) -> str:
        domain = module.split(".")[1]
        return f"{PUBLIC_PREFIX if domain in public else PACKAGE_PREFIX}{module}"

    for py_file in (directory / "zqnt").rglob("*"):
        if py_file.suffix not in (".py", ".pyi") or "/v3/" not in py_file.as_posix():
            continue
        src = py_file.read_text()
        if py_file.suffix == ".py":
            patched = py_import.sub(lambda m: f"{m[1]} {prefixed(m[2])}", src)
            patched = builder.sub(lambda m: f"{m[1]}{PACKAGE_PREFIX}{m[2]}", patched)
        else:
            patched = pyi_ref.sub(lambda m: prefixed(m[1]), src)
        if patched != src:
            py_file.write_text(patched)


if __name__ == "__main__":
    check_pin()
    shutil.rmtree(GENERATED, ignore_errors=True)
    with tempfile.TemporaryDirectory() as protos:
        export_protos(Path(protos))
        generate_v2(Path(protos) / "internal" / "v2", Path(protos) / "public" / "v2")
        generate_v3(Path(protos) / "internal" / "v3", Path(protos) / "public" / "v3")
    print("Done.")
