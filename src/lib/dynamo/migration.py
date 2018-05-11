from lib.dynamo.client import DynamoClientManager


async def table_exists(name: str) -> bool:
    """Check if table exists."""
    async with DynamoClientManager() as dynamodb:
        try:
            await dynamodb.describe_table(TableName=name)
        except dynamodb.exceptions.ResourceNotFoundException:
            state = False
        else:
            state = True
    # allow the Context Manager to exit
    return state


async def ensure_table(schema: dict):
    """Ensure the table exists."""
    table_name = schema.get('TableName')
    if not table_name:
        return

    exists = await table_exists(table_name)
    if exists:
        return

    async with DynamoClientManager() as dynamodb:
        await dynamodb.create_table(**schema)
        waiter = dynamodb.get_waiter('table_exists')
        await waiter.wait(TableName=table_name)


async def delete_table(schema: dict):
    """Deletes the table."""
    table_name = schema.get('TableName')
    if not table_name:
        return

    exists = await table_exists(table_name)
    if not exists:
        return

    async with DynamoClientManager() as dynamodb:
        await dynamodb.delete_table(TableName=table_name)
        waiter = dynamodb.get_waiter('table_not_exists')
        await waiter.wait(TableName=table_name)
