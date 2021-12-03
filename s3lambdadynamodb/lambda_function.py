import json
import s3dynamodbhelper

#Driver Module
def lambda_handler(event, context):
    
    #01.Find Uploaded Bucket & Object Names
    bucketName,objectName=s3dynamodbhelper.findBucketObjectNames(event)
    jsonData=s3dynamodbhelper.get_data_from_object(bucketName,objectName)
    
    print("______________________________________")
    result=s3dynamodbhelper.insertIntoDynamoDB(jsonData)
    print("Inserted: ",s3dynamodbhelper.DYNAMODB_TABLE_NAME)
    print("______________________________________")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Welcome from Lambda!')
    }
