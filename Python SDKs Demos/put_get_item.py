# Slide 36/37 of Module 6 of Developing on AWS
# Need to run 'pip install boto3' from terminal first
# In Cloud9, run with Python 3

import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('users')

responsePut = table.put_item(
  Item={
    'username': 'janedoe',
    'first_name': 'Jane',
    'last_name': 'Doe',
    'age': 25,
    'account_type': 'standard_user'
  }
)

print("PUT RESPONSE")
print(responsePut)

responseGet = table.get_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)

print("\nGET RESPONSE")
print(responseGet)

#item = responseGet['Item']
#print(item)