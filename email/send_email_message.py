import json
import boto3

client = boto3.client("sqs")
queue_url = "https://sqs.us-east-1.amazonaws.com/249804032116/Skate_Queue"


def lambda_handler(event, context):
    sent_to = event["email"]["sent_to"]
    body = event["email"]["body"]

    formattedEmail = {"sent_to": sent_to, "body": body}

    message = client.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(formattedEmail),
    )

    return {"statusCode": 200, "body": json.dumps(message, indent=2)}
