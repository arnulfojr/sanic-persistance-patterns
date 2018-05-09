from sanic import response
from sanic.request import Request

from lib.mysql.db import manager

from todo.blueprint import blueprint
from todo.models import ToDo
from todo.schemas import ToDoSchema


todo_schema = ToDoSchema()


@blueprint.route('/', methods=['GET'])
async def get_all(request: Request):
    all_todos = await manager.execute(ToDo.select())
    payload = list()
    for todo in all_todos:
        # do simple deserialization
        dumped, _ = todo_schema.dump(todo)
        payload.append(dumped)

    return response.json(payload)


@blueprint.route('/', methods=['POST'])
async def add_todo(request: Request):
    body = request.json

    # validate income request
    todo_schema.load(body)

    todo = await manager.create(ToDo, **body)
    payload, errors = todo_schema.dump(todo)

    return response.json(payload, status=201)
