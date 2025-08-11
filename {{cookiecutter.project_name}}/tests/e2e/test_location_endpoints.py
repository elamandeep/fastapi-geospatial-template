from fastapi.testclient import TestClient


def test_create_location(client: TestClient):
    response = client.post(
        "/location/create/",
        json={"name": "Test Place", "coordinates": [77.5946, 12.9716]},
    )
    print(response.status_code)
    assert response.status_code == 201
    data = response.json()

    assert "id" in data
    assert data["name"] == "Test Place"
