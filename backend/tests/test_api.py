from fastapi.testclient import TestClient
from main import app

def test_earnings_endpoint():
  client = TestClient(app)

  response = client.get("/earnings")

  assert response.status_code == 200

  data = response.json()

  assert "today_earnings" in data
  assert "since_nov1_2025" in data
  assert "total_earnings" in data

  assert isinstance(data["today_earnings"], int)
  assert isinstance(data["since_nov1_2025"], int)
  assert isinstance(data["total_earnings"], int)