"""Shared helpers for the per-array closure tests (``test_closure*.py``).

Each array's decomposition/budget closures live in their own ``test_closure_<array>.py``
so that populating the vocabulary's closures later is a matter of matching one test file to
one array. The only genuinely shared piece is locating the (uncommitted, large) provider
source file, which every closure test needs.
"""

import os
from pathlib import Path


def resolve_data(env: str, filename: str) -> Path | None:
    """Return a local path to a provider source file, or ``None`` to skip the test.

    Looks at the ``env`` environment variable first, then the cached download locations
    (``~/.amocatlas_data`` and ``/tmp``). The source files are not committed (large / zipped
    downloads), so a closure test skips unless the file is available locally.
    """
    candidates = [os.environ.get(env)] if os.environ.get(env) else []
    candidates += [
        Path.home() / ".amocatlas_data" / filename,
        Path("/tmp") / filename,
    ]
    for c in candidates:
        if c and Path(c).is_file():
            return Path(c)
    return None
