import marshmallow


class ToDoSchema(marshmallow.Schema):
    """ToDo Schema."""
    id = marshmallow.fields.UUID(dump_only=True)

    text = marshmallow.fields.String(required=True)

    created_on = marshmallow.fields.DateTime(dump_only=True)
