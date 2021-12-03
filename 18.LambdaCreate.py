import boto3
import json

iam=boto3.client("iam")

# role_policy={
#   "Version": "2012-10-17",
#   "Statement": [
#     {
#       "Sid": "",
#       "Effect": "Allow",
#       "Principal": {
#         "Service": "lambda.amazonaws.com"
#       },
#       "Action": "sts:AssumeRole"
#     }
#   ]
# }

# response=iam.create_role(RoleName="rl03decmujahedv2",
# AssumeRolePolicyDocument=json.dumps(role_policy)
# )

role=iam.get_role(RoleName="rl03decmujahed")
print("----------")
print(role["Role"]["Arn"])
print("----------")
lambdaClient=boto3.client("lambda")
zipped_code=""
with open("lambda.zip","rb") as f:
  zipped_code=f.read()
print("----zippedCode Created------")

response=lambdaClient.create_function(
  FunctionName="fn03decmujahedvv",
  Runtime="python3.8",
  Role=role["Role"]["Arn"],
  Handler="handler.lambda_handler",
  Code=dict(ZipFile=zipped_code),
  Timeout=300
)
print("----------")
print(response)

