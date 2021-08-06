# aws-demos

This is a package of demo resources for use in AWS training courses. It includes an AWS CloudFormation YAML template, demo scripts, this readme, the original presentation for its debut, and auxillary demo files. Multiple demos are wrapped together.

by Harrison Sherwin (hasherwi@amazon.com)

First, see my presentation here that's also in this package (Sherwin_Demos_Presentation.pptx).

Comments, Questions, and Bug Reports can be sent to: hasherwi@amazon.com.

PREREQUISITES:
  - Permissions are needed for all resource creation.
  - Make sure you have permissions to add S3 Bucket Policies on a per bucket basis.
  - (Optional) Deploy a Route 53 hosted zone if you'll be using a domain.

DEPLOYMENT STEPS:
  1. Deploy the template to create the CloudFormation stack.
    AWS CLI Command Example Without Domain Deployment:
      aws cloudformation deploy --template-file C:\Users\hasherwi\Downloads\Sherwin_TIPS_Demo\Sherwin_Demos.yaml --stack-name tips-demo --capabilities CAPABILITY_NAMED_IAM --parameter-overrides NumberOfAZs=2 NumberOfNATs=2  InitialWebServerCapacity=4
    AWS CLI Command Example With Domain Deployment:
      aws cloudformation deploy --template-file C:\Users\hasherwi\Downloads\Sherwin_TIPS_Demo\Sherwin_Demos.yaml --stack-name tips-demo --capabilities CAPABILITY_NAMED_IAM --region us-east-1 --parameter-overrides NumberOfAZs=2 NumberOfNATs=2 OwnedDomainName="hsherwin.com" OwnedHostedZoneId="Z0687820MAF0GNYEQVR8" InitialWebServerCapacity=4
  2. (Optional) Add static web components to the auto-generated S3 bucket.

KNOWN ISSUES:
  - Rarely, removing AZs during stack modification can fail to delete public subnets related to ALB ENIs.
    --No workaround known, manually delete the ALB.

  - When using a domain, a hosted zone is required to already exist. This is the only current dependency because domains purchased outside of Route 53 require advance notice of name server configurations.
    --No workaround, create the hosted zone before stack deployment.

  - A common limit that can halt deployment is Elastic IPs. By default, every account has a limit of 5 EIPs per region.
    --Workaround 1: Request a service quota increase before deployment.
    --Workaround 2: Deploy fewer NAT Gateways.
    --Planned Resolution: Construct a Lambda function to check if deployment will result in a service quota violation, and if so, request the increase via the AWS API.

  - Selecting more AZs than exist in the region will result in a stack failure with the following error, where # is replaced with the number of AZs available:
    --Template error: Fn::Select cannot select nonexistent value at index #
    --No known workaround.

  - create_table.py fails on the Cloud9 instance because of a defined session_token in the credentials file.
    --Workaround: Remove the session_token.
    
  -Because a static call is made to deploy the certificates in us-east-1, the stack is currently deployable only in the commerical partition:
    --Workaround: Deploy demos only in the commerical partition.

PLANNED IMPROVEMENTS:
  - Standalone Functionality:
    Create storyline template to point to smaller scoped templates.

  - More Functionality:
    Add cross-VPC TGW demo.
    Add ECS/EKS/ECR/Fargate demos.
    Add API Gateway demos.
    Add Step Functions demos.
    Add RDS demos.
    Add DynamoDB demos.
    Add EFS demos.
    Add Cognito demos.
    Add CloudTrail demos.
    Add SQS demos.
    Add more advanced ALB rules.
    Add SNS demos.
    Add Auto Scaling Group Policies.
    Add LB functionality when using only one AZ, if possible.
    Add VPC Flow Logs.
    Add other CloudWatch Resources.
    Automatically personalize the index.html page using AWS Lambda.

  - More Validation:
    Check if the requested AZ count exceeds the region AZ count.
    Check if the ARN is valid in lambda for creating the cert for sending success.
    Check if the lambda certificate calls actually worked

  - Transition from Deprecated Functionality:
    Remove ForwardedValues from CloudFront resources for CachePolicyId.

  - DynamoDB Python Code:
    Fix known issue with session_token.
    Import more data into table.
    Add more query and scan scenarios.

  - Security Improvements:
    Tighten the S3 Cleaner Lambda Policies.
    Tighten the Cert Creator Lambda Policies.
    Tighten the S3 bucket policies to only allow CloudFront to get certain extensions.
    Add WAF.
    Tighten the wildcard certificates to specific subdomain certificates.
    Update sample S3 objects for HTTPS.

  - Efficient Resource Usage:
    Optimize CIDR block usage.
    Consolidate CloudFront Distributions.

  - More User Choice:
    Add Secondary VPC deployment choice.
    
  - Multi-Partition Support.

RELEASE NOTES:
  - Version 2.0, 06 August 2021:
    Scope:
      #TODO: All of the below
      Create smaller, standalone subset templates.
      Enhance documentation for above changes.
      Add architecture diagrams to documentation.
    Added functionality to the lambda function interacting with S3 to fill the bucket.
      Upgraded to Python 3.8
      #TODO: Write the fill code.
      #TODO: Test the code.
    Created a lambda to call the certificates to be created in us-east-1 so the demo can occur be deployed with a domain cross-regionally.
      #TODO: Test the creation code.
      #TODO: Write the deletion code.
      #TODO: Test the deletion code.
    Added validation of the Route 53 Hosted Zone parameter.
      "Type: AWS::Route53::HostedZone::Id" from "Type: String".
    Added use of the AWS::Partition pseudo parameter in webServerRole.
    Change file and directory names to remove "Sherwin".
    Change sample index.html file header from "hsherwin.com" to "My Webpage".
      All the links are still specific to this domain (for now), but it should be more palatable now for other instructors in quick scenarios.

  - Version 1.3, 19 July 2021:
    Added Python SDK demos for use with EC2 and DynamoDB.
    Added demo script: S3 CLI.
    Readded Cloud9 installation.
      It now uses SSH and the public subnet.
    Added ElastiCache demo components.
      Added pip and redis-py installation to EC2 instances user data.
      New ElastiCache cluster, EC2 security group and ElastiCache subnet group.
      Output for cluster endpoint address.
      Demo script.
    Now redirecting HTTP to HTTPS for CloudFront distributions.
    The web servers now support HTTPS when behind the ALB.
      Modified security groups to allow HTTPS traffic.
      Added an ALB listener for HTTPS traffic.
    Added DynamoDB VPC Interface Endpoint.
    Simplified S3 Cleanup Lambda Function to remove unnecessary code.
    Added output for S3 bucket name.
      This is mostly a proof of concept for getting an auto-generated bucket's name.
    Minor fix to EC2 user data to close HTML tags on index.html page.
    Additional inline template documentation.
    Metadata grammar edits.

  - Version 1.2, 07 July 2021:
    Removed Cloud9 instance temporarily.
    Added resources to empty (and allowing deletion of) the S3 bucket on stack deletion.
      Source: https://gist.github.com/drumadrian/e1601ab34e7f609b5075f65599108960
    Added Second VPC for future use.
    Added DynamoDB table for future use.
    Enabled Versioning for the S3 Bucket.
    Trimmed all trailing whitespace.
    Resolved Issue where the wrong Route Table was associated with Private Subnet F.
    Swapped Public Subnet B through F creation to be based on NAT count and not AZ count. So resources are no longer created unnecessarily. Modified downstream dependencies as needed.

  - Version 1.1, 29 June 2021:
    Bug Fix where lb-cache subdomain was unusable.
    Added Cloud9 Instance deployment.

  - Version 1.0, 22 June 2021:
    Initial Release.
