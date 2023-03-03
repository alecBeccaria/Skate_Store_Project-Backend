import boto3
from os import getenv
import json


region_name = getenv("APP_REGION")

users_table = boto3.resource(
    'dynamodb',
    region_name=region_name).Table('Users')


def lambda_handler(event, context):
    print(event)
    User = read_event(event)

    users_table.put_item(Item=User)
    return User


def read_event(event):
    username = event['username']
    password = event['password']
    email = event['email']
    cart = []

    User = {
        "username": username,
        "password": password,
        "email": email,
        "cart": cart
    }

    return User
