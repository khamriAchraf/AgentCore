import pytest
from httpx import ASGITransport, AsyncClient

from agentcore.app import create_app
from agentcore.config import Settings


@pytest.mark.anyio
async def test_health_endpoints_do_not_require_external_services() -> None:
    app = create_app(Settings())

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as client:
        live_response = await client.get("/health/live")
        ready_response = await client.get("/health/ready")

    assert live_response.status_code == 200
    assert live_response.json() == {"status": "ok"}
    assert ready_response.status_code == 200
    assert ready_response.json() == {"status": "ready"}


def test_asgi_entrypoint_imports() -> None:
    from agentcore.main import app

    assert app.title == "AgentCore"
