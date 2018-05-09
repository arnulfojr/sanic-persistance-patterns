from sanic.request import Request
from sanic import response

import aioboto3

from lib.dynamo.client import DYNAMO_CONFIG
from reminder.blueprint import blueprint


@blueprint.route('/', methods=['GET'])
async def get_reminders(request: Request):
    async with aioboto3.resource('dynamodb', **DYNAMO_CONFIG) as db:
        table = db.Table('reminders')
        results = await table.scan()
    return response.json(results.get('Items'), 200)


@blueprint.route('/', methods=['POST'])
async def save_reminder(request: Request):
    async with aioboto3.resource('dynamodb', **DYNAMO_CONFIG) as db:
        table = db.Table('reminders')
        reminder = request.json
        await table.put_item(Item=reminder)
    return response.json(reminder, 201)
