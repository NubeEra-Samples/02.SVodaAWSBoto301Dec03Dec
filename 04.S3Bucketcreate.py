import boto3
s3=boto3.client("s3")
response=s3.create_bucket(Bucket="bkt0337mujahed")
print("check with :   aws s3 ls ")