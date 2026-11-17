"""Application settings."""

from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Validated settings that do not require external services in Phase 1."""

    model_config = SettingsConfigDict(
        env_prefix="AGENTCORE_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = Field(default="AgentCore", min_length=1, max_length=80)
    environment: Literal["local", "test", "demo"] = "local"
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "INFO"
