import json
def lambda_handler(event,context):
    return {
        'statusCode':200,
        'body':json.dumps('Welcome my boto3 lambda v2 function')
    }