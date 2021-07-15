#This illustrates a single AWS API action through three interfaces.

#First, demo the EC2 dashboard in the AWS Management Console.
#Second, demo the equivalent AWS CLI call:
#   aws ec2 describe-instances
#Third, demo this code in Cloud9, run with Python 3

import boto3
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)