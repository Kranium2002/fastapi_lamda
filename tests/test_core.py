from fastapi.testclient import TestClient
from api.main import app
import sys, asyncio

if sys.platform == "win32" and (3, 8, 0) <= sys.version_info < (3, 9, 0):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

client = TestClient(app)
def test_root():
    response = client.get("/")
    assert response.status_code == 200

    
  