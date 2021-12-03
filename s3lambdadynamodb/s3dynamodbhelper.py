import os
import boto3
import logging
import json

DYNAMODB_TABLE_NAME=os.environ.get("DB_TABLE_NAME","defaultMujahedTable")

def findBucketObjectNames(event):
    bucketName=""
    objectName=""
    for record in event["Records"]:
        bucketName=record["s3"]["bucket"]["name"]
        objectName=record["s3"]["object"]["key"]
    return (bucketName,objectName)

def get_data_from_object(bucketName,objectName):
    s3=boto3.client("s3")
    response=s3.get_object(Bucket=bucketName,Key=objectName)
    content=response["Body"]
    jsondata=json.loads(content.read())
    return jsondata

def insertIntoDynamoDB(item):
    dynamodb=boto3.resource("dynamodb")
    table=dynamodb.Table(DYNAMODB_TABLE_NAME)
    response=table.put_item(
        Item=item
        )
    print(response)
    return True