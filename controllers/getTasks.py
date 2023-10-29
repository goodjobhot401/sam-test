import json

def getTasks(event, context):

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Getting all tasks successfully!"
        }),
    }