import boto3

def fnCreateDefaultVPC(vpcClient):
    from botocore.exceptions import ClientError
    vpcId="Not Set"
    try:
        response=vpcClient.create_default_vpc()
        vpcId=response["Vpc"]["VpcId"]
        print("Created Default VPC")
    except ClientError:
        print("Not Possible to Create")
    return vpcId

#Driver Code- Workflow
if __name__=="__main__":
    vpcclient=boto3.client("ec2")
    vpcId=fnCreateDefaultVPC(vpcclient)    
    print( vpcId )