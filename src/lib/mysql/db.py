import peewee_async
import settings


database = peewee_async.PooledMySQLDatabase(settings.mysql.DATABASE,
                                            host=settings.mysql.ENDPOINT,
                                            port=settings.mysql.PORT,
                                            user=settings.mysql.USER,
                                            password=settings.mysql.PASSWORD)


manager = peewee_async.Manager(database)
