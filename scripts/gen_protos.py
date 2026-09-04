#!/usr/bin/env python3
"""
Generate Python protobuf / gRPC stubs from the platform's canonical proto source.

Source: ../zqnt-utils/src/main/proto/ (this repo lives at zqnt-platform/utils/zqnt-utils-python,
a sibling of zqnt-platform/utils/zqnt-utils — same source Java and the Go SDKs generate from).
Historically this pulled from a separate `zqnt-protos` GitHub repo (vendored as a git submodule);
that repo tracks a pre-refactor schema (still the old Mission/Task/Scheduler service, missing the
capability-execution-*.proto files entirely) and is no longer used.

Pin: PROTO_REF below pins that sibling checkout to an exact ref before generating, and restores it
to whatever it was afterwards -- same mechanism zqnt-utils-golang's own scripts/gen_protos.sh uses
(see that script's own comment), and the same reason: don't silently generate from whatever the
sibling happens to be checked out to. Currently a branch name (LOCAL-DEV-ONLY -- see PROTO_REF's
own comment); a real release must point this at an immutable tag instead.

Output: zqnt_utils/generated/zqnt/
Usage:  python scripts/gen_protos.py
"""

import subprocess
import sys
from pathlib import Path

try:
    from grpc_tools import protoc
except ImportError:
    sys.exit("grpcio-tools is required: pip install grpcio-tools")

ROOT = Path(__file__).resolve().parent.parent
PROTO_DIR = ROOT.parent / "zqnt-utils" / "src" / "main" / "proto"
OUT_DIR = ROOT / "zqnt_utils" / "generated" / "zqnt"

WELL_KNOWN_PROTOS = Path(protoc.__file__).parent / "_proto"

# zqnt-protos' own `1.3.1` tag -- the real, immutable release this repo's own v1.3.1 is the
# Python counterpart of (adds simulator-control.proto/SimulatorControlService on top of the 1.3.0
# wire contract; cherry-picked onto the real 1.3.0 tag, not main, which has diverged onto the
# 2.0.0-track proto -- see zqnt-protos' own tag message). Same resolve-then-assert pattern
# zqnt-utils-golang's own gen_protos.sh uses: resolve the tag, assert it's still the exact commit
# expected, fail loudly if it's moved, rather than silently generating from whatever it now
# points to.
PROTO_TAG = "1.3.1"
PROTO_TAG_COMMIT = "8c2d5a42a97b54f915e39c38b0cd12cb188a5be1"


def _git(*args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(PROTO_DIR), *args],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def _pin_proto_ref() -> str:
    """Checks PROTO_DIR out to PROTO_TAG, fetching it first if not already present locally, and
    asserting it still resolves to PROTO_TAG_COMMIT (fail loudly if the tag has moved). Returns
    the commit PROTO_DIR was on before, so the caller can restore it afterwards."""
    original_commit = _git("rev-parse", "HEAD")
    verify = subprocess.run(
        ["git", "-C", str(PROTO_DIR), "rev-parse", "--verify", "--quiet", f"refs/tags/{PROTO_TAG}"],
        capture_output=True,
    )
    if verify.returncode != 0:
        print(f"Fetching zqnt-protos tag {PROTO_TAG}...")
        _git("fetch", "--quiet", "origin", f"refs/tags/{PROTO_TAG}:refs/tags/{PROTO_TAG}")

    resolved_commit = _git("rev-parse", f"refs/tags/{PROTO_TAG}^{{commit}}")
    if resolved_commit != PROTO_TAG_COMMIT:
        sys.exit(
            f"zqnt-protos tag {PROTO_TAG} resolves to {resolved_commit}, not the expected "
            f"{PROTO_TAG_COMMIT} -- the tag has moved since this script was last updated. "
            "Refusing to generate from an unverified commit; update PROTO_TAG_COMMIT above once "
            "you've confirmed the new target is actually what you want."
        )

    print(f"Pinning proto submodule to zqnt-protos {PROTO_TAG} ({resolved_commit}, currently {original_commit})...")
    _git("checkout", "--quiet", PROTO_TAG)
    return original_commit


def _restore_proto_ref(original_commit: str) -> None:
    print(f"Restoring proto submodule to {original_commit}...")
    _git("checkout", "--quiet", original_commit)


def ensure_init_files(directory: Path) -> None:
    for dirpath in [directory.parent, directory]:
        init = dirpath / "__init__.py"
        if not init.exists():
            init.write_text("")


def run() -> None:
    if not PROTO_DIR.exists():
        sys.exit(
            f"Canonical proto source not found at {PROTO_DIR} — this script must be run from a "
            "checkout of zqnt-platform, with zqnt-utils-python at utils/zqnt-utils-python "
            "(i.e. a sibling of utils/zqnt-utils)."
        )

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ensure_init_files(OUT_DIR)

    proto_files = sorted(PROTO_DIR.glob("*.proto"))
    if not proto_files:
        sys.exit(f"No .proto files found in {PROTO_DIR}")

    print(f"Generating {len(proto_files)} proto file(s) -> {OUT_DIR.relative_to(ROOT)}")

    args = [
        "grpc_tools.protoc",
        f"--proto_path={PROTO_DIR}",
        f"--proto_path={WELL_KNOWN_PROTOS}",
        f"--python_out={OUT_DIR}",
        f"--pyi_out={OUT_DIR}",
        f"--grpc_python_out={OUT_DIR}",
        f"--mypy_grpc_out={OUT_DIR}",
        *[str(p) for p in proto_files],
    ]

    rc = protoc.main(args)
    if rc != 0:
        sys.exit(f"protoc failed with exit code {rc}")

    # grpc_tools generates absolute imports; rewrite them to relative so the
    # package works when installed as zqnt_utils.generated.zqnt.*
    _fix_imports(OUT_DIR)

    print("Done.")


def _fix_imports(directory: Path) -> None:
    """
    grpc_tools emits absolute imports that only work if the output dir is on
    sys.path. Rewrite them to relative imports so the package works when
    installed as zqnt_utils.generated.zqnt.*:

      `import common_pb2 as common__pb2`  ->  `from . import common_pb2 as common__pb2`
      `from base_pb2 import *`            ->  `from .base_pb2 import *`

    The second form is emitted for `import public "base.proto";` (public
    re-exports) and must be rewritten too, or the module fails to import.
    """
    import re

    bare_import = re.compile(r"^import (\w+_pb2) as (\w+)$", re.MULTILINE)
    public_import = re.compile(r"^from (\w+_pb2) import \*$", re.MULTILINE)

    for py_file in [*directory.glob("*.py"), *directory.glob("*.pyi")]:
        src = py_file.read_text()
        patched = bare_import.sub(r"from . import \1 as \2", src)
        patched = public_import.sub(r"from .\1 import *", patched)
        if patched != src:
            py_file.write_text(patched)
            print(f"  fixed imports in {py_file.name}")


if __name__ == "__main__":
    original_commit = _pin_proto_ref()
    try:
        run()
    finally:
        _restore_proto_ref(original_commit)
