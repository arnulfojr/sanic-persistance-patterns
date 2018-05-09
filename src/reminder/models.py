

class MixinModel(dict):

    __tablename__ = 'mixin_model'

    @classmethod
    def schema(cls):
        raise NotImplemented


class Reminder(MixinModel):
    """Reminder object."""
    __tablename__ = 'reminders'

    @classmethod
    def schema(cls):
        return {
            'TableName': cls.__tablename__,
            'AttributeDefinitions': [
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                }
            ],
            'KeySchema': [
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                }
            ],
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        }
