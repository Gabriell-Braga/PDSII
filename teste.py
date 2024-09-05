from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "LALA"}

def test_quadrado():
    response = client.get("/quadrado/5")
    assert response.status_code == 200
    assert response.json() == {"Quadrado": 25}