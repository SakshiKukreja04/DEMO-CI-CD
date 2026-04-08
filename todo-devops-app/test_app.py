from itertools import count

import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["TASKS"] = []
    app.config["TASK_ID_COUNTER"] = count(1)
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Pulse Tasks" in response.data


def test_add_task(client):
    response = client.post("/tasks", data={"task": "Test Task"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Test Task" in response.data


def test_blank_task_is_ignored(client):
    response = client.post("/tasks", data={"task": "   "}, follow_redirects=True)
    assert response.status_code == 200
    assert b"No tasks yet" in response.data


def test_delete_task(client):
    client.post("/tasks", data={"task": "Delete Me"}, follow_redirects=True)
    response = client.post("/tasks/1/delete", follow_redirects=True)
    assert response.status_code == 200
    assert b"Delete Me" not in response.data
