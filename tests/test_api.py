from fastapi.testclient import TestClient

from aquatwin.api import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["module"] == "AT-MORT-001"


def test_synthetic_observation_keeps_synthetic_marker():
    response = client.post(
        "/v1/observations",
        json={
            "cage_id": "00000000-0000-0000-0000-000000000001",
            "cohort_id": "00000000-0000-0000-0000-000000000002",
            "observed_at": "2026-08-27T12:00:00Z",
            "variable_code": "oxygen_mg_l",
            "value": 8.1,
            "unit": "mg/L",
            "source_id": "synthetic-ci",
            "synthetic": True
        },
    )
    assert response.status_code == 200
    body = response.json()
    assert body["synthetic"] is True
    assert body["quality_flag"] == "PASS"
