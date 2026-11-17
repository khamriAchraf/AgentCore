from pathlib import Path

import pytest
from pydantic import ValidationError

from agentcore.config import Settings


def test_settings_have_local_defaults_without_environment(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.chdir(tmp_path)
    for variable in (
        "AGENTCORE_APP_NAME",
        "AGENTCORE_ENVIRONMENT",
        "AGENTCORE_LOG_LEVEL",
    ):
        monkeypatch.delenv(variable, raising=False)

    settings = Settings()

    assert settings.app_name == "AgentCore"
    assert settings.environment == "local"
    assert settings.log_level == "INFO"


def test_settings_read_prefixed_environment_variables(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("AGENTCORE_APP_NAME", "AgentCore Test")
    monkeypatch.setenv("AGENTCORE_ENVIRONMENT", "test")
    monkeypatch.setenv("AGENTCORE_LOG_LEVEL", "DEBUG")

    settings = Settings()

    assert settings.app_name == "AgentCore Test"
    assert settings.environment == "test"
    assert settings.log_level == "DEBUG"


def test_settings_read_dotenv_file(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    (tmp_path / ".env").write_text("AGENTCORE_APP_NAME=FromDotEnv\n", encoding="utf-8")
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("AGENTCORE_APP_NAME", raising=False)

    assert Settings().app_name == "FromDotEnv"


@pytest.mark.parametrize(
    "values",
    [
        {"app_name": ""},
        {"environment": "production"},
        {"log_level": "TRACE"},
    ],
)
def test_settings_reject_invalid_values(values: dict[str, str]) -> None:
    with pytest.raises(ValidationError):
        Settings.model_validate(values)
