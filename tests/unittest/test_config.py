from importlib import reload

from app.core import config


def test_to_bool():
    """Test that to_bool converts strings to boolean values."""
    assert config.to_bool("yes") is True
    assert config.to_bool("1") is True
    assert config.to_bool("true") is True
    assert config.to_bool("y") is True
    assert config.to_bool("YES") is True
    assert config.to_bool("Y") is True

    assert config.to_bool("no") is False
    assert config.to_bool("0") is False
    assert config.to_bool("false") is False
    assert config.to_bool("n") is False
    assert config.to_bool("NO") is False
    assert config.to_bool("N") is False
    assert config.to_bool("invalid") is False


def test_settings(monkeypatch):
    """Test that config.Settings() uses environment variables if set."""
    c = config.Settings()

    assert c.LOG_LEVEL == "INFO"
    assert c.LOG_USE_BASIC_FORMAT is False
    assert c.API_PREFIX == "/deloitte/genai/api"

    monkeypatch.setenv("LOG_LEVEL", "DEBUG")
    monkeypatch.setenv("LOG_USE_BASIC_FORMAT", "False")
    monkeypatch.setenv("API_PREFIX", "/custom/api")
    reload(config)

    c = config.Settings()

    assert c.LOG_LEVEL == "DEBUG"
    assert c.LOG_USE_BASIC_FORMAT is False
    assert c.API_PREFIX == "/custom/api"
