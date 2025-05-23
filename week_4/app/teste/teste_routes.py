import pytest
from httpx import AsyncClient
from ..app import app

@pytest.mark.asyncio
async def test_read_router():
    async with AsyncClient(app=app, base_url="http://localhost:8000/espclient/") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg":"HELLO WORLD"}

@pytest.mark.asyncio
async def test_login_invalid():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            "espclient/login",
            data={"username": "teste010", "password": "teste010"},
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
    assert response.status_code == 401