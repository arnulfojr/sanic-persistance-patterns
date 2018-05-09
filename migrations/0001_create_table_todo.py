"""
create table todo
date created: 2018-05-08 21:50:51.641659
"""


def upgrade(migrator):
    with migrator.create_table('todo') as table:
        table.uuid('id', constraints=['PRIMARY KEY'])
        table.char('text', max_length=255)
        table.datetime('created_on')


def downgrade(migrator):
    migrator.drop_table('todo')
