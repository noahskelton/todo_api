from flask import Flask, jsonify, request, Response
import json
from typing import Dict
import uuid

app = Flask(__name__)
import json
from flask.testing import FlaskClient
from typing import List, Dict, Generator
data: Dict[str, str] = {}


@app.route('/todo', methods=['GET'])
def get_todos() -> Response:

    return Response(
        response=json.dumps(data),
        mimetype="application/json",
    )

@app.route('/todo/<string:obj_id>', methods=['GET'])
def get_todo(obj_id: str) -> Response:
    if obj_id not in data:
        return Response(
            status=404
        )
    return Response(
        response=json.dumps(data[obj_id]),
        mimetype="application/json",
    )


@app.route('/todo', methods=['POST'])
def create_todo() -> Response:
    payload = request.form
    obj_id = uuid.uuid4().hex
    data[obj_id] = payload["text"]

    return Response(
        response=json.dumps({"obj_id":obj_id}),
        mimetype="application/json",
        status=201
    )


@app.route('/todo/<string:obj_id>', methods=['PATCH'])
def edit_todo(obj_id: str) -> Response:

    if obj_id not in data:
        return Response(
            status=404
        )

    payload = request.form
    data[obj_id] = payload["text"]


    return Response()


@app.route('/todo/<string:obj_id>', methods=['DELETE'])
def delete_todo(obj_id: str) -> Response:

    if obj_id not in data:
        return Response(
            status=404
        )
    del data[obj_id]

    return Response()


if __name__ == '__main__':  # pragma: no cover
    app.run()