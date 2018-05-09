import os


USER = os.getenv('MYSQL_USER')

PASSWORD = os.getenv('MYSQL_PASSWORD')

PORT = int(os.getenv('MYSQL_PORT'))

ENDPOINT = os.getenv('MYSQL_ENDPOINT')

DATABASE = os.getenv('MYSQL_DATABASE')

URL = f'mysql://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}'
