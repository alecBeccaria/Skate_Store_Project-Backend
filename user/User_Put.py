import boto3
from os import getenv

region_name = getenv("APP_REGION")


def lambda_handler(event, context):
    username = event['params']['path']['username']
    password = event['body-json']['password']
    email = event['body-json']['email']
    cart = event['body-json']['cart']

    key = {
        'username': username
    }

    users_table = boto3.resource(
        'dynamodb', region_name=region_name).Table('Users')
    response = users_table.update_item(
        UpdateExpression='set password=:p, email=:e, cart=:c',
        ExpressionAttributeValues={
            ':p': password,
            ':e': email,
            ':c': cart
        },
        Key=key,
        ReturnValues="UPDATED_NEW"
    )

    return response['Attributes']
