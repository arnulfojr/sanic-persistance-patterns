from sanic import Blueprint
from sanic.request import Request
from sanic import response


blueprint = Blueprint('health', url_prefix='/health')


@blueprint.route('/', methods=['GET'])
async def ok(request: Request):
    return response.json({'status': True})
