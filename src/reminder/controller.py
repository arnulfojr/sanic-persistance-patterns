from sanic.request import Request

from lib.dynamo.client import DynamoClientManager
from reminder.blueprint import blueprint


@blueprint.route('/', methods=['GET'])
async def get_reminders(request: Request):
    async with DynamoClientManager() as db:
        db.
