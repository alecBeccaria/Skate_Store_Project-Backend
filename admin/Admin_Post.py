import boto3
from os import getenv


region_name = getenv("APP_REGION")

admins_table = boto3.resource(
    'dynamodb',
    region_name=region_name).Table('Admins')


def lambda_handler(event, context):
    Admin = read_event(event)
    
    admins_table.put_item(Item=Admin)
    return Admin


def read_event(event):
    username = event['username']
    password = event['password']
    email = event['email']

    Admin = {
        "username": username,
        "password": password,
        "email": email
    }

    return Admin
