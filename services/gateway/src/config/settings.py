from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


GATEWAY_ENV_FILE = Path(__file__).resolve().parents[2] / ".env"


class GatewaySettings(BaseSettings):
    """Gateway service configuration sourced from environment variables or .env files."""

    environment: str = "local"
    host: str = "0.0.0.0"
    port: int = 8000
    log_level: str = "info"

    model_config = SettingsConfigDict(
        env_prefix="gateway_",
        env_file=str(GATEWAY_ENV_FILE),
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


@lru_cache(maxsize=1)
def load_gateway_settings() -> GatewaySettings:
    """Load and cache gateway settings."""
    return GatewaySettings()
