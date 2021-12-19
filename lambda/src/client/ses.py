import boto3
from botocore.exceptions import ClientError
import os
import src.model.email_template as email_template

def send_email(destination_address:str, gift_receiver_name:str) -> str:
    email_text = f'The person you are giving a gift to is: {gift_receiver_name}'
    email_body = email_template.template.format(email_text=email_text)

    client = boto3.client('ses',region_name=os.environ["AWS_REGION"])

    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    destination_address
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': "UTF-8",
                        'Data': email_body,
                    },
                    'Text': {
                        'Charset': "UTF-8",
                        'Data': email_text,
                    },
                },
                'Subject': {
                    'Charset': "UTF-8",
                    'Data': "Secret Santa Raffle",
                },
            },
            Source=os.getenv("SES_EMAIL_FROM")
        )
    except ClientError as e:
        print(e.response['Error']['Message'])

    return f"Successfully sent email to {destination_address}"