from logging import Logger, basicConfig, getLogger, DEBUG, INFO, StreamHandler
from os import environ
from sys import stdout

from pythonjsonlogger.jsonlogger import JsonFormatter

_DEBUG = environ.get("DEBUGGING", "false").lower() == "true"
_LEVEL = DEBUG if _DEBUG else INFO
_SKIP_ATTRS = (
    "args",
    "asctime",
    "created",
    "exc_info",
    "exc_text",
    "levelno",
    "module",
    "msecs",
    "msg",
    "pathname",
    "process",
    "processName",
    "relativeCreated",
    "stack_info",
    "thread",
    "threadName",
)


def _configure_logging() -> None:
    _json_handler = StreamHandler(stream=stdout)
    _formatter = JsonFormatter(
        reserved_attrs=_SKIP_ATTRS,
        timestamp=True,
    )
    _json_handler.setFormatter(_formatter)

    basicConfig(
        handlers=[_json_handler],
        level=_LEVEL,
        force=True,
    )


def get_logger(name: str) -> Logger:
    """
    Returns standard Logger
    """

    return getLogger(name=name)


_configure_logging()
