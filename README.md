# Secret Santa
Secret Santa raffle. Sends email to every participant informing them who their gift receiver is.

# Architecture

Lambda function that gets an event of the form ```{
  "participants": [
    {
      "name": "a",
      "email": "a@a.com"
    },
    ...
  ]
}```
It uses boto3 to send the emails with a verified identity email as sender.

# Prerequisites
1. Configure an email on AWS SES as verified identity
2. Configure a profile on ~/.aws

# How to run

1. Run `cdk deploy` on the infra folder
2. Trigger the lambda function with the event specified in the [ Architecture](#architecture) containing the participants through the AWS console
