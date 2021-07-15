# Slide 40/41 of Module 6 of Developing on AWS
# Need to run 'pip install boto3' from terminal first
# In Cloud9, run with Python 3

import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('users')

responseQuery = table.query(
    KeyConditionExpression=Key('username').eq('janedoe')
)

print("FULFILLED QUERY RESPONSE")
print(responseQuery)

responseQueryEmpty = table.query(
    KeyConditionExpression=Key('username').eq('johndoe')
)

print("\nEMPTY QUERY RESPONSE")
print(responseQueryEmpty)

responseScan = table.scan(
    FilterExpression=Attr('age').lt(27)
)

print("\nSCAN RESPONSE")
print(responseScan)