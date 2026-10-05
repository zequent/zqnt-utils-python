#!/usr/bin/env python3
"""
Generate Python protobuf / gRPC stubs from the platform's contracts, zqnt-protos.

Source: ./proto -- this repo's own submodule of github.com/Zequent/zqnt-protos, the same layout
zqnt-utils-golang uses. It used to read the Java repo's submodule as a sibling directory
(../zqnt-utils/src/main/proto), pinned by a branch name; that branch was deleted after the 2.0.0
merge, so generation broke on any fresh checkout. Owning the submodule means generation works in
any clone (`git submodule update --init proto`) and depends on exactly one recorded commit.

zqnt-protos has two proto roots (see its README):
  proto/v2  frozen 2.x contracts, byte-identical to 2.0.0 -> zqnt_utils/generated/zqnt/*_pb2.py
            (unchanged module names: zqnt_utils.generated.zqnt.base_pb2, ...)
  proto/v3  zqnt.<domain>.v3 packages -> zqnt_utils/generated/zqnt/<domain>/v3/*_pb2.py
            (zqnt_utils.generated.zqnt.capability.v3.command_pb2, ...)

Pin: the submodule pointer staged in this repo's index; what is checked out must be it. A commit
without a release tag (a preview from a zqnt-protos PR branch) is refused unless ALLOW_UNTAGGED=1.
To move: `git -C proto fetch && git -C proto checkout <tag> && git add proto`, re-run, commit the
pointer together with the regenerated code. Run with PYTHONDONTWRITEBYTECODE=1 (generated/ tracks
no bytecode of its own and should not gain any).

Usage:  python scripts/gen_protos.py
"""

import os
import re
import subprocess
import sys
from pathlib import Path

try:
    from grpc_tools import protoc
except ImportError:
    sys.exit("grpcio-tools is required: pip install grpcio-tools")

ROOT = Path(__file__).resolve().parent.parent
PROTO_DIR = ROOT / "proto"
V2_DIR = PROTO_DIR / "v2"
V3_DIR = PROTO_DIR / "v3"
GENERATED = ROOT / "zqnt_utils" / "generated"
V2_OUT = GENERATED / "zqnt"
PACKAGE_PREFIX = "zqnt_utils.generated."

WELL_KNOWN_PROTOS = Path(protoc.__file__).parent / "_proto"


def _git(*args: str, cwd: Path = ROOT) -> str:
    return subprocess.run(
        ["git", "-C", str(cwd), *args], check=True, capture_output=True, text=True
    ).stdout.strip()


def check_pin() -> None:
    """The checked-out contract must be the recorded one, and a release unless explicitly a preview."""
    if not (V2_DIR / "common.proto").exists():
        sys.exit(
            f"Proto submodule is not checked out (or predates the v2/v3 layout) at {PROTO_DIR} -- "
            "run: git submodule update --init proto"
        )
    recorded = _git("ls-files", "-s", "proto").split()[1]
    current = _git("rev-parse", "HEAD", cwd=PROTO_DIR)
    if current != recorded:
        sys.exit(
            f"The proto submodule is at {current}, but this repo records {recorded}. Run "
            "'git submodule update proto' to restore it, or 'git add proto' to move the pin."
        )
    tag = subprocess.run(
        ["git", "-C", str(PROTO_DIR), "describe", "--tags", "--exact-match"],
        capture_output=True,
        text=True,
    )
    if tag.returncode == 0:
        print(f"Generating from zqnt-protos {tag.stdout.strip()} ({current})...")
    elif os.environ.get("ALLOW_UNTAGGED") == "1":
        print(f"Generating from untagged zqnt-protos {current} (preview, ALLOW_UNTAGGED=1)...")
    else:
        sys.exit(
            f"zqnt-protos {current} carries no release tag. Pin a tag, or set ALLOW_UNTAGGED=1 for a "
            "preview from a zqnt-protos PR branch (it must move to the tag after the release)."
        )


def _protoc(proto_root: Path, out: Path, files: list[Path]) -> None:
    args = [
        "grpc_tools.protoc",
        f"--proto_path={proto_root}",
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


def generate_v2() -> None:
    files = sorted(V2_DIR.glob("*.proto"))
    print(f"v2: {len(files)} proto file(s) -> {V2_OUT.relative_to(ROOT)}")
    V2_OUT.mkdir(parents=True, exist_ok=True)
    ensure_init_files(V2_OUT, GENERATED)
    _protoc(V2_DIR, V2_OUT, files)
    _fix_v2_imports(V2_OUT)


def generate_v3() -> None:
    files = sorted(V3_DIR.rglob("*.proto"))
    print(f"v3: {len(files)} proto file(s) -> {GENERATED.relative_to(ROOT)}/zqnt/<domain>/v3")
    _protoc(V3_DIR, GENERATED, files)
    for proto in files:
        ensure_init_files(GENERATED / proto.relative_to(V3_DIR).parent, GENERATED)
    _fix_v3_imports(GENERATED)


def _fix_v2_imports(directory: Path) -> None:
    """
    grpc_tools emits absolute imports that only work if the output dir is on sys.path. Rewrite
    them to relative imports so the package works when installed as zqnt_utils.generated.zqnt.*:

      `import common_pb2 as common__pb2`  ->  `from . import common_pb2 as common__pb2`
      `from base_pb2 import *`            ->  `from .base_pb2 import *`

    The second form is emitted for `import public "base.proto";` (public re-exports) and must be
    rewritten too, or the module fails to import.
    """
    bare_import = re.compile(r"^import (\w+_pb2) as (\w+)$", re.MULTILINE)
    public_import = re.compile(r"^from (\w+_pb2) import \*$", re.MULTILINE)

    for py_file in [*directory.glob("*.py"), *directory.glob("*.pyi")]:
        src = py_file.read_text()
        patched = bare_import.sub(r"from . import \1 as \2", src)
        patched = public_import.sub(r"from .\1 import *", patched)
        if patched != src:
            py_file.write_text(patched)


def _fix_v3_imports(directory: Path) -> None:
    """
    v3 files import each other by package path (`from zqnt.capability.v3 import capability_pb2`).
    Prefix those with zqnt_utils.generated. so they resolve inside this package. In .py files only
    the import lines and the module name handed to the descriptor builder are touched -- the
    serialized descriptor itself also contains "zqnt.capability.v3" and must stay byte-exact. The
    .pyi stubs carry no descriptor, so their type references are rewritten throughout.
    """
    v3_module = r"zqnt\.[a-z_]+\.v3"
    py_import = re.compile(rf"^(from|import) ({v3_module})", re.MULTILINE)
    builder = re.compile(rf"(BuildTopDescriptorsAndMessages\(DESCRIPTOR, ')({v3_module})")
    pyi_ref = re.compile(rf"(?<![\w.])({v3_module})")

    for py_file in (directory / "zqnt").rglob("*"):
        if py_file.suffix not in (".py", ".pyi") or "/v3/" not in py_file.as_posix():
            continue
        src = py_file.read_text()
        if py_file.suffix == ".py":
            patched = py_import.sub(rf"\1 {PACKAGE_PREFIX}\2", src)
            patched = builder.sub(rf"\1{PACKAGE_PREFIX}\2", patched)
        else:
            patched = pyi_ref.sub(rf"{PACKAGE_PREFIX}\1", src)
        if patched != src:
            py_file.write_text(patched)


if __name__ == "__main__":
    check_pin()
    generate_v2()
    generate_v3()
    print("Done.")
