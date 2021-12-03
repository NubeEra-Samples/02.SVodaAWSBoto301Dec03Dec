import boto3
class DynamoDBHelper:
    def __init__(self) -> None:
        dynamodb=boto3.resource("dynamodb")
        self.table=dynamodb.Table("dyt1mujahed")
    def insertItem(self,item):
        response=self.table.put_item(Item=item)
        return response

    def insertItems(self,items):
        with self.table.batch_writer() as b:
            b.put_item(Item=items[0])
            b.put_item(Item=items[1])
            b.put_item(Item=items[2])
            print(b)
        
    def getItem(self,ky):
        response=self.table.get_item(Key=ky)
        return response["Item"]

    def getAllScan(self):
        response=self.table.scan()
        return response

    def deleteItem(self,item):
        response=self.table.delete_item(Key=item)
        return response

    def getName(self,name):
        from boto3.dynamodb.conditions import Key
        response=self.table.query(KeyConditionExpression=Key("Name").eq("Mujahed"))
        return response
