import boto3
import json

#01. Select IAM Role
iam=boto3.client("iam")
role=iam.get_role(RoleName="rl03decmujahed")
print("----------")

#02. Create Lambda.zip File
dir_name=r"C:\Practicals\02.SVodaAWSBoto301Dec03Dec\serverlessarchi"
output_file="lambda"
import shutil
shutil.make_archive(output_file,'zip',dir_name)
print("Zip Created kindly Check...")

#03. Convert lambda.zip into Object
zipped_code=""
with open("lambda.zip","rb") as f:
  zipped_code=f.read()
print("----zippedCode Created------")

# 04. Create Lambda Function using Parameters
lambdaClient=boto3.client("lambda")
response=lambdaClient.create_function(
  FunctionName="fn03decmujahedv3",
  Runtime="python3.8",
  Role=role["Role"]["Arn"],
  Handler="handler.lambda_handler",
  Code=dict(ZipFile=zipped_code),
  Timeout=300
)
print("----------")
print(response)

