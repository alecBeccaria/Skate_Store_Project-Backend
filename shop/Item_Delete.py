import boto3
from boto3.dynamodb.conditions import Attr
from os import getenv

region_name = getenv("APP_REGION")


def lambda_handler(event, context):

    id = event['params']['path']['item_id']

    key = {
        'id': id
    }

    items_table = boto3.resource(
        'dynamodb', region_name=region_name).Table('Items')
    items_table.delete_item(Key=key)

    return {
        'message': 'Deleted item from database',
        'key': key
    }
