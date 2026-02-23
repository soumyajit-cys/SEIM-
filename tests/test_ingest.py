import pytest
from httpx import AsyncClient
from api.main import app

@pytest.mark.asyncio
async def test_ingest():

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/ingest", json={
            "source": "linux-auth",
            "host": "localhost",
            "log": "Failed password for root from 1.1.1.1 port 22",
            "timestamp": "2026-02-19T10:00:00"
        })

    assert response.status_code == 200