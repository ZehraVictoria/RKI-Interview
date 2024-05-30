from fastapi.testclient import TestClient

from rki.interview.main import app

client = TestClient(app)


def test_read_candidates() -> None:
    response = client.get("/candidates")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "full_name": "Lisa Simpson",
            "experiences": ["Saxophonist","Fast food vendor"],
            "birthday": None,
        },
        {
            "id": 2,
            "full_name": "Ned Flanders",
            "experiences": ["Pharmaceutical salesmen"],
            "birthday": None,
        },
        {
            "id": 3,
            "full_name": "Bernd das Brot",
            "experiences": ["TV host","Motivational speaker"],
            "birthday": None,
        },
    ]
