import boto3
from os import getenv

region_name = getenv("APP_REGION")


def lambda_handler(event, context):
    response = read()
    return response


def read():
    # gets Database resource
    dynamodb = boto3.resource('dynamodb', region_name=region_name)
    items_table = dynamodb.Table('Items')

    response = items_table.scan()
    return response['Items']
