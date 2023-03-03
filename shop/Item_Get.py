import boto3
from os import getenv

region_name = getenv("APP_REGION")


def lambda_handler(event, context):
    print(event)
    response = read(event)
    return response


def read(event):
    # gets Database resource
    item_id = event['params']['path']['item_id']

    dynamodb = boto3.resource('dynamodb', region_name=region_name)
    items_table = dynamodb.Table('Items')

    key = {
        'id': item_id
    }

    Db_Item = items_table.get_item(Key=key)
    Item = Db_Item['Item']
    return Item
