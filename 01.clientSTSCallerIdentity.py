#1. Import Packages
import json
import boto3

#2. Create Client
objClient=boto3.client('sts')

#3. Request Features/Options
response=objClient.get_caller_identity()

#4. Extract details
userId=response["UserId"]
account=response['Account']
arn=response['Arn']
#5. Display Data
output={ 
    "UserId":userId ,
    "Account":account ,
    "Arn":arn
    }
print(json.dumps(output,indent=4))