import boto3
from os import getenv

region_name = getenv("APP_REGION")


def lambda_handler(event, context):
    print(event)
    response = read(event)
    return response


def read(event):
    # gets Database resource
    username = event["params"]["path"]["username"]

    dynamodb = boto3.resource("dynamodb", region_name=region_name)
    admins_table = dynamodb.Table("Users")

    key = {"username": username}

    Item = admins_table.get_item(Key=key)
    admin = Item["Item"]
    return {
        'statusCode': 200,
        'body': admin
    }
