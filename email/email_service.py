import smtplib
import os
import json


def lambda_handler(event, context):
    # sent_to is a list of emails to send to.
    sent_emails = []

    for record in event["Records"]:
        record_body = json.loads(record["body"])
        print(record_body)

        sent_to = record_body["sent_to"]
        body = record_body["body"]
        print(body)
        print(sent_to)

        email = send_email(sent_to, body)
        sent_emails.append(email)

    return {"statusCode": 200, "body": sent_emails}


# SEND EMAIL FUNCTION
def send_email(sent_to, body):
    gmail_user = "abecc2255@gmail.com"
    gmail_app_password = os.environ.get("GMAIL_APP_PASSWORD")
    sent_from = gmail_user
    sent_to = sent_to
    sent_subject = "Skate Store!"
    sent_body = body

    email_text = """\
From: %s
To: %s
Subject: %s
%s
""" % (
        sent_from,
        ", ".join(sent_to),
        sent_subject,
        sent_body,
    )

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(gmail_user, gmail_app_password)
        server.sendmail(sent_from, sent_to, email_text.encode("utf-8"))
        server.close()
        print(email_text)
        print("Email sent!")
        return email_text
    except Exception as exception:
        print("Error: %s!\n\n" % exception)
