##client --> delete_bucket(), resource --> bucket.delete()

import boto3

# s3client=boto3.client("s3")
# s3client.delete_bucket(Bucket="bkt0337mujahed")
# print("Bucket Deleted")

# s3resource=boto3.resource("s3")
# bucketName=input("Enter Bucket Name to Delete: ")
# Bucket=s3resource.Bucket(bucketName)
# Bucket.delete()
# print("Bucket Deleted")

s3resource=boto3.resource("s3")
bucketName="bktd10458mujahed"
Bucket=s3resource.Bucket(bucketName)

def cleanup_bucket_objects(myBucket):
    # Delete All Objects
    for obj in myBucket.objects.all():
        obj.delete()
    # If Object has version Delete version with objects
    for objVer in myBucket.object_versions.all():
        objVer.delete()

#Delete All Objects From Bucket
cleanup_bucket_objects(Bucket)

#Delete an Empty Bucket
Bucket.delete()
