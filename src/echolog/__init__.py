import sys
if sys.version_info < (3, 9):
    raise RuntimeError("EchoLog requires Python 3.9 or higher.")

from .logs import (
    infoLog,
    warnLog,
    errorLog,
    successLog,
    requestLog,
    inputLog,
    holdLog,
    maskedLog,
    debugLog,
)

__all__ = [
    "infoLog",
    "warnLog",
    "errorLog",
    "successLog",
    "requestLog",
    "inputLog",
    "holdLog",
    "maskedLog",
    "debugLog",
]
