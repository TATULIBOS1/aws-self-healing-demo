from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    assert False  # Force failure
   ## response = client.get("/")
   ## assert response.status_code == 200
   ## assert response.json() == {"message": "Welcome to the CI/CD demo"}
