from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_health_endpoint():
    """Test that the health endpoint returns successfully."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "operational",
        "message": "BudgetronAI AI Service Operational"
    }