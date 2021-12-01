#1. Import Packages
import boto3

#2. Create Client
objClient=boto3.client('iam')

#3. Request Features/Options  API=GetPaginator/ListRoles    boto3= get_paginator(list_roles)
objPaginator=objClient.get_paginator('list_roles')

#print(type(objPaginator) )
#print( objPaginator )

for page in objPaginator.paginate():
    for r in page['Roles']:
        print( r["RoleName"] )