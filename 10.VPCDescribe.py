import boto3
vpcClient=boto3.client("ec2") #vpc-0165db4801ceaab19, us-east-1  vpc64mujahed

def fnVPCDescribe(tagKey,tagValues,maxItems=5):
    from botocore.exceptions import ClientError
    vpcLists=[]
    try:
        paginator=vpcClient.get_paginator("describe_vpcs")
        response_iterator=paginator.paginate(Filters=[
            {
                'Name':f'tag:{tagKey}',
                'Values':tagValues
            }
            ],PaginationConfig={'MaxItems':maxItems})
        full_result=response_iterator.build_full_result()
        for page in full_result["Vpcs"]:
            vpcLists.append(page)
        print("Listing VPC Done")
    except ClientError as ce:
        print("Found Error: ",ce)
    return vpcLists

#Driver Code- Workflow
if __name__=="__main__":
    vpcLists=fnVPCDescribe(tagKey="Name",tagValues=["vpc64mujahed","vpcds","Nikhil","nishivpc93"],maxItems=10)    
    import json
    for vpc in vpcLists:
        print( json.dumps(vpc,indent=4) )