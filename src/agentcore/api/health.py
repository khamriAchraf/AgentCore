"""Health endpoints."""

from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/health", tags=["health"])


class HealthResponse(BaseModel):
    status: Literal["ok", "ready"]


@router.get("/live", response_model=HealthResponse)
def live() -> HealthResponse:
    """Report that the process is running."""
    return HealthResponse(status="ok")


@router.get("/ready", response_model=HealthResponse)
def ready() -> HealthResponse:
    """Report that the Phase 1 application is ready to serve requests."""
    return HealthResponse(status="ready")
