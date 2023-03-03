import boto3
from os import getenv
from uuid import uuid4


region_name = getenv("APP_REGION")

items_table = boto3.resource(
    'dynamodb',
    region_name=region_name).Table('Items')


def lambda_handler(event, context):
    Item = read_event(event)

    items_table.put_item(Item=Item)
    return Item


def read_event(event):
    id = str(uuid4())
    name = event['name']
    category = event['category']
    price = event['price']
    description = event['description']
    manufacturer = event['manufacturer']
    image = event['image']

    Item = {
        "id": id,
        "name": name,
        "category": category,
        "price": price,
        "description": description,
        "manufacturer": manufacturer,
        "image": image
    }

    return Item
