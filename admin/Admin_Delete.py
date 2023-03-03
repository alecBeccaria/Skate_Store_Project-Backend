import boto3
from boto3.dynamodb.conditions import Attr
from os import getenv

region_name = getenv("APP_REGION")


def lambda_handler(event, context):

    username = event['params']['path']['username']

    key = {
        'username': username
    }

    admins_table = boto3.resource(
        'dynamodb', region_name=region_name).Table('Admins')
    admins_table.delete_item(
        ConditionExpression=Attr('username').eq(username),
        Key=key
    )

    return {
        'message': 'Deleted admin from database',
        'key': key
    }
