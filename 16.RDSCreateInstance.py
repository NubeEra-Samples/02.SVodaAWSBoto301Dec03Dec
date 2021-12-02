import boto3

rds=boto3.client("rds")

response=rds.create_db_instance(
    AllocatedStorage=5,
    DBInstanceClass="db.t2.micro",
    DBInstanceIdentifier="dbv1mujahed",
    Engine="MySQL",
    MasterUserPassword="testpwd0021",
    MasterUsername="admin01"
)

print(response)