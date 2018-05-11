Sanic using Persistence layer
=============================

Spoiler alert!
--------------

NoSQL usage with PynamoDB (an ORM-like for DynamoDB) is only supported with sync (i.e. Flask, Sanic is async) code.

There's no migrations for DynamoDB but making simple migrations can be easily done.

Peewee offers more async support than SQLAlchemy's ORM.


DynamoDB
--------

Use of aiobotocore and aioboto3.

- botocore http://botocore.readthedocs.io/en/latest/index.html
- boto3 http://boto3.readthedocs.io/en/stable/guide/dynamodb.html
- aioboto3 (but refer to boto3 docs) https://aioboto3.readthedocs.io/en/latest/readme.html

Migrations in NoSQL
-------------------

Migrations in NoSQL are kind of missleading, but the requirements are pretty much basic when talking DynamoDB.

To ensure tables are present, as DynamoDB requires it, a simple `ensure_table` method is required to create a table and avoiding to recreate and fail. In the same sense, downgrading would be deleting the table `delete_table` method is therefore present.

Updating indexes can be done in that sense, first ensuring the base table exists then updating the table indexes using botocore's API.

Therefore a simple `upgrade` and `downgrade` method is required.

For the full research, please refer to:

- http://sadalage.com/blog/2014/10/14/migrations-in-nosql-databases/
- http://dynamodb-mapper.readthedocs.io/en/latest/api/migration.html


ORM
---

Usage of ORM through peewee.

- peewee: http://docs.peewee-orm.com/en/2.10.2/peewee/quickstart.html
- Async peewee lib: http://peewee-async.readthedocs.io/en/latest/peewee_async/examples.html
- Migrations: http://peewee-moves.readthedocs.io/en/latest/usage.html


Schema Validation
-----------------

- http://marshmallow.readthedocs.io/en/latest/examples.html#examples
