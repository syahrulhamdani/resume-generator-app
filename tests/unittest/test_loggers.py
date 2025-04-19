"""Unit tests for app.core.loggers module."""
from unittest.mock import patch

from app.core.loggers import setup_logging


@patch('logging.config.dictConfig')
def test_setup_logging_default_params(mock_dict_config):
    """Test setup_logging with default parameters."""
    setup_logging()

    # Verify dictConfig was called
    mock_dict_config.assert_called_once()

    # Get the configuration passed to dictConfig
    config = mock_dict_config.call_args[0][0]

    # Verify default parameters
    assert config["loggers"][""]["level"] == "INFO"
    assert "stdout" in config["loggers"][""]["handlers"]
    assert "stderr" in config["loggers"][""]["handlers"]
    assert "stdout-basic" not in config["loggers"][""]["handlers"]
    assert "stderr-basic" not in config["loggers"][""]["handlers"]

@patch('logging.config.dictConfig')
def test_setup_logging_custom_level(mock_dict_config):
    """Test setup_logging with custom log level."""
    setup_logging(log_level="DEBUG")

    # Get the configuration passed to dictConfig
    config = mock_dict_config.call_args[0][0]

    # Verify custom log level
    assert config["loggers"][""]["level"] == "DEBUG"

@patch('logging.config.dictConfig')
def test_setup_logging_basic_format(mock_dict_config):
    """Test setup_logging with basic format enabled."""
    setup_logging(use_basic_format=True)

    # Get the configuration passed to dictConfig
    config = mock_dict_config.call_args[0][0]

    # Verify basic formatters are used
    assert "stdout-basic" in config["loggers"][""]["handlers"]
    assert "stderr-basic" in config["loggers"][""]["handlers"]
    assert "stdout" not in config["loggers"][""]["handlers"]
    assert "stderr" not in config["loggers"][""]["handlers"]

@patch('logging.config.dictConfig')
def test_setup_logging_custom_level_and_format(mock_dict_config):
    """Test setup_logging with both custom level and basic format."""
    setup_logging(log_level="ERROR", use_basic_format=True)

    # Get the configuration passed to dictConfig
    config = mock_dict_config.call_args[0][0]

    # Verify both customizations
    assert config["loggers"][""]["level"] == "ERROR"
    assert "stdout-basic" in config["loggers"][""]["handlers"]
    assert "stderr-basic" in config["loggers"][""]["handlers"]
