import boto3
from os import getenv
from boto3.dynamodb.conditions import Attr

region_name = getenv("APP_REGION")


def lambda_handler(event, context):
    response = read(event)
    return response


def read(event):
    # gets Database resource
    search = event["params"]["path"]["search_term"]

    dynamodb = boto3.resource("dynamodb", region_name=region_name)
    items_table = dynamodb.Table("Items")

    Db_Category_Items = items_table.scan(
        FilterExpression=Attr("name").contains(search)
        | Attr("description").contains(search)
    )
    Search_Items = Db_Category_Items["Items"]
    return Search_Items
