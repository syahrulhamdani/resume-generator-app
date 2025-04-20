"""Utility module."""
import logging
import os

_LOGGER = logging.getLogger(__name__)


async def remove_file(path: str):
    """Remove a file by path.

    Args:
        path (str): The file path to remove.
    """
    _LOGGER.info("Removing file: %s", path)
    try:
        if os.path.exists(path):
            os.unlink(path)
            _LOGGER.debug("Done removing file: %s", path)
    except Exception as exc:
        _LOGGER.exception("Error removing file: %s", exc)
    return path
