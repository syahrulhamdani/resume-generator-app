"""Utilities for handling configuration values.

Functions:
  to_bool(value: str) -> bool:
    Converts a string to a boolean value.

    Args:
      value: The string to convert. If the string is "yes", "true", "y", or "1",
        the function returns True. Otherwise, it returns False.

    Returns:
      A boolean value of the string value.
"""
import os

from pydantic_settings import BaseSettings


def to_bool(value: str) -> bool:
    """Converts a string to a boolean value.

    Args:
        value: The string to convert. If the string is "yes", "true", "y",
            or "1", the function returns True. Otherwise, it returns False.

    Returns:
        A boolean value of the string value
    """
    if value.lower() in ["yes", "true", "y", "1"]:
        return True
    return False


class AppSettings(BaseSettings):
    """Application-level settings."""
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_USE_BASIC_FORMAT: bool = to_bool(
        os.getenv("LOG_USE_BASIC_FORMAT", "False")
    )
    API_PREFIX: str = os.getenv("API_PREFIX", "/deloitte/genai/api")


class Settings(AppSettings):
    """All configuration settings"""


config = Settings()
