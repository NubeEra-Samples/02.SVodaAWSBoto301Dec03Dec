import boto3

vpcResource=boto3.resource("ec2")

groupName="sgsamplebasicusage"
vpcId="vpc-0f99163c0bfce8255"

response=vpcResource.create_security_group(
    Description="creating for demo purpose",
    GroupName=groupName,
    VpcId=vpcId,
    TagSpecifications=[{
        "ResourceType":"security-group",
        "Tags":[{'Key':'Name','Value':groupName}]
    }]
    )

print(response.id) #sg-06c6dc520c80cbc48