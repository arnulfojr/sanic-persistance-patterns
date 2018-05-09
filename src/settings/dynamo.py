"""DynamoDB variables"""
import os


REGION = os.getenv('AWS_REGION')

ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')

SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

ENDPOINT = os.getenv('AWS_DYNAMODB_ENDPOINT')
