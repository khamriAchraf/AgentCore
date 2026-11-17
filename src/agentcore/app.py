"""FastAPI application factory."""

from fastapi import FastAPI

from agentcore.api.health import router as health_router
from agentcore.config import Settings


def create_app(settings: Settings | None = None) -> FastAPI:
    """Create the API application without connecting to external services."""
    app_settings = settings if settings is not None else Settings()
    application = FastAPI(title=app_settings.app_name, version="0.1.0")
    application.include_router(health_router)
    return application
