def test_read_main(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_get_output(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "Worldd"}
