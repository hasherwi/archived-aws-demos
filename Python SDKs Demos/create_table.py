# Slide 34 of Module 6 of Developing on AWS
# Need to run 'pip install boto3' from terminal first
# In Cloud9, run with Python 3
# Show 'aws dynamodb list-tables' first from command line to show table is not yet created

import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='users',
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'last_name',
            'KeyType': 'RANGE'        
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'last_name',
            'AttributeType': 'S'        
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

#table.meta.client.get_waiter('table exists').wait(TableName='users')

print(table)