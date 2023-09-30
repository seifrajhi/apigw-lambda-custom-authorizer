import json

def hello_world(event, context):
    # Assuming authentication has already been done
    # You can access the authenticated user's information
    # from the event object or context if needed.

    # Your logic here
    response = {
        "statusCode": 200,
        "body": json.dumps({"message": "Hello, World!"}),
    }

    return response

