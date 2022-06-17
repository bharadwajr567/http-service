def test_set_name(client):
    expected = {
        "message": "Name changed!",
        "old_name": None,
        "new_name": "TEST",
    }
    response = client.post(
        "/set_name",
        json={"name": "TEST"},
    )
    assert response.status_code == 201
    assert response.json == expected
    expected["old_name"] = "TEST"
    expected["new_name"] = "TEST2"
    response = client.post(
        "/set_name",
        json={"name": "TEST2"},
    )
    assert response.status_code == 201
    assert response.json == expected
