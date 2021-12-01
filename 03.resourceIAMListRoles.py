import boto3

objResource=boto3.resource("iam")

for r in objResource.roles.all():
    print(r.name)