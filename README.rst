Sanic using Persistence layer
=============================

Spoiler alert!
--------------
NoSQL usage with PynamoDB (an ORM-like for DynamoDB) is only supported with sync (i.e. Flask, Sanic is async) code.

There's no migrations for DynamoDB but making simple migrations can be easily done.


DynamoDB
--------

Use of aiobotocore and aioboto3


ORM
---

Usage of ORM through peewee.

- peewee: http://docs.peewee-orm.com/en/2.10.2/peewee/quickstart.html
  - Async lib: http://peewee-async.readthedocs.io/en/latest/peewee_async/examples.html
- Migrations: http://peewee-moves.readthedocs.io/en/latest/usage.html


Schema Validation
-----------------

- http://marshmallow.readthedocs.io/en/latest/examples.html#examples
