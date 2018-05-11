import botocore.config
import aiobotocore
import settings


DYNAMO_CONFIG = {
    'region_name': settings.dynamo.REGION,
    'aws_access_key_id': settings.dynamo.ACCESS_KEY_ID,
    'aws_secret_access_key': settings.dynamo.SECRET_ACCESS_KEY,
    'endpoint_url': settings.dynamo.ENDPOINT,
    'config': botocore.config.Config(retries=dict(max_attempts=2))
}

# use asyncio's default loop
session = aiobotocore.get_session()


# create a dynamodb client
def client(config: dict = DYNAMO_CONFIG):
    """Returns a DynamoDB Client."""
    return session.create_client('dynamodb', **config)


class DynamoClientManager:
    """Async Client Manager."""

    def __init__(self, **kwargs):
        """
        :param kwargs: keyword argument to pass to the client
        """
        self.cfg = kwargs or DYNAMO_CONFIG
        self._client = None

    async def __aenter__(self):
        if self._client:
            return self._client
        self._client = client(self.cfg)
        return self._client

    async def __aexit__(self, exc_type, exc, tb):
        # TODO: log the exception
        if self._client:
            await self._client.close()
