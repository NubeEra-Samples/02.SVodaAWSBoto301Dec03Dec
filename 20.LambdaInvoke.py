import boto3
import json

test_event={
  "name": "mujahed",
  "key2": "value2",
  "key3": "value3"
}

lambdaClient=boto3.client("lambda")

response=lambdaClient.invoke(FunctionName="fn03decmujahedv3",Payload=json.dumps(test_event))
response2=lambdaClient.invoke(FunctionName="fn03decmujahedv4",Payload=json.dumps(response))

print( response["Payload"] )
print( response["Payload"].read().decode("utf-8") )