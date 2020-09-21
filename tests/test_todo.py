import json
from flask.testing import FlaskClient
from typing import List, Dict


class TestList:
    def test_empty(self, client: FlaskClient) -> None:
        res = client.get('/todo')
        data = res.get_json()
        expected_data: None = None
        assert data == expected_data

    def test_not_empty(self, client: FlaskClient) -> None:
        client.post('/todo', data={"text": "test_text", "obj_id": 0})
        res = client.get('/todo', data={"obj_id": 0})
        data = res.get_json()
        expected_data = 'test_text'
        assert data == expected_data

    def test_edit(self, client: FlaskClient) -> None:
        client.post('/todo', data={"text": "test_text", "obj_id": 1})
        client.patch('/todo', data={"text": "test_text_edited", "obj_id": 1})
        res = client.get('/todo', data={"obj_id": 1})
        data = res.get_json()
        expected_data = "test_text_edited"
        assert data == expected_data


