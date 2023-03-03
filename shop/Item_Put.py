import boto3
from boto3.dynamodb.conditions import Attr
from os import getenv

region_name = getenv("APP_REGION")


def lambda_handler(event, context):

    id = event['params']['path']['item_id']
    # body elements
    name = event['body-json']['name']
    category = event['body-json']['category']
    price = event['body-json']['price']
    description = event['body-json']['description']
    manufacturer = event['body-json']['manufacturer']
    image = event['body-json']['image']

    key = {
        'id': id
    }

    items_table = boto3.resource(
        'dynamodb', region_name=region_name).Table('Items')
    response = items_table.update_item(
        UpdateExpression='set name=:n, category=:c, price=:p, description=:d, manufacturer=:m, image=:i',
        ExpressionAttributeValues={
            ':n': name,
            ':c': category,
            ':p': price,
            ':d': description,
            ':m': manufacturer,
            ':i': image
        },
        Key=key,
        ReturnValues="UPDATED_NEW"
    )

    return response['Attributes']
