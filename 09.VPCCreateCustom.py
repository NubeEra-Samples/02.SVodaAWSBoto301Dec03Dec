import boto3

def fnCreateCustomVPC(vpcResource,IpCidr):
    from botocore.exceptions import ClientError
    vpcId="Not Set"
    try:
        response=vpcResource.create_vpc(CidrBlock=IpCidr,
        InstanceTenancy="default",
        TagSpecifications=[{"ResourceType":"vpc","Tags":[{'Key':'Name','Value':'vpc64mujahed'}]}]
        )
        vpcId=response.id
        print("Created Custom VPC")
    except ClientError:
        print("Not Possible to Create Custom VPC")
    return vpcId

#Driver Code- Workflow
if __name__=="__main__":
    vpcresource=boto3.resource("ec2") #vpc-0165db4801ceaab19, us-east-1  vpc64mujahed
    ip_cidr="192.168.0.0/26" #64
    vpcId=fnCreateCustomVPC(vpcresource,ip_cidr)    
    print( vpcId )