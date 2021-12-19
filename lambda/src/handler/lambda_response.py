import json


def ok(pairs: dict):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"pairs": pairs}),
    }


def bad_request(error_message=""):
    return {
        "statusCode": 400,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"errorMessaage": error_message, "pairs": {}}),
    }
