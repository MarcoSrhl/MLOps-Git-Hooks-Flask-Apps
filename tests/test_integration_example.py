from app import app


def test_index_endpoint_returns_200_and_contains_form():

    client = app.test_client()

    # to call the index route
    response = client.get("/")
    #the server should respond with 200 OK
    assert response.status_code == 200
    assert b"<form" in response.data
