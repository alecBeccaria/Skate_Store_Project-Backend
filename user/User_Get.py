import boto3
from os import getenv
import json

region_name = getenv("APP_REGION")


def lambda_handler(event, context):
    print(event)
    response = read(event)
    return response


def read(event):
    # gets Database resource
    username = event["params"]["path"]["username"]

    dynamodb = boto3.resource("dynamodb", region_name=region_name)
    admins_table = dynamodb.Table("Admins")
    users_table = dynamodb.Table("Users")

    key = {"username": username}

    try:
        Item = admins_table.get_item(Key=key)
        print(Item)
        if Item["Item"] != None:
            print("admin found!")
            return {"statusCode": 200, "body": Item["Item"]}
    except Exception as e:
        print(e)
        try:
            Item = users_table.get_item(Key=key)
            if Item["Item"] != None:
                print("user found!")
                return {"statusCode": 200, "body": Item["Item"]}

        except Exception as e:
            print(e)
            return {"statusCode": 400, "body": "User not found in db"}

    
