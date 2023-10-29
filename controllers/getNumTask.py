import json

def getNumTask(event, context):
    id = event["pathParameters"]["id"]

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Here's the task No.{id}"
        }),
    }