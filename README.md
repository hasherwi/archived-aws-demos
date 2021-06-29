# aws-demos
https://github.com/hasherwi/aws-demos/blob/main/README.md

THIS IS AN AWS CLOUDFORMATION YAML TEMPLATE FOR DEPLOYING AN END-TO-END WEB SERVER ARCHITECTURE ON AWS. IT IS INTENDED TO BE USED PURELY FOR TECHNICAL TRAINING AND SELF-LEARNING PURPOSES.
by Harrison Sherwin (hasherwi@amazon.com)

First, see my presentation here that's also in this package (Sherwin_Demos_Presentation.pptx).

Comments, Questions, and Bug Reports can be sent to: hasherwi@amazon.com.

PREREQUISITES:
  - Make sure you have permissions to add S3 Bucket Policies on a per bucket basis.
  - (Optional) Deploy a Route 53 hosted zone if you'll be using a domain.

DEPLOYMENT STEPS:
  1. Deploy the template to create the CloudFormation stack. Use region us-east-1 if you plan to deploy a domain.
    AWS CLI Command Example Without Domain Deployment:
      aws cloudformation deploy --template-file C:\Users\hasherwi\Downloads\Sherwin_TIPS_Demo\Sherwin_Demos.yaml --stack-name tips-demo --capabilities CAPABILITY_NAMED_IAM --parameter-overrides NumberOfAZs=2 NumberOfNATs=2  InitialWebServerCapacity=4
    AWS CLI Command Example With Domain Deployment:
      aws cloudformation deploy --template-file C:\Users\hasherwi\Downloads\Sherwin_TIPS_Demo\Sherwin_Demos.yaml --stack-name tips-demo --capabilities CAPABILITY_NAMED_IAM --region us-east-1 --parameter-overrides NumberOfAZs=2 NumberOfNATs=2 OwnedDomainName="hsherwin.com" OwnedHostedZoneId="Z0687820MAF0GNYEQVR8" InitialWebServerCapacity=4
  2. (Optional) Add static web components to the auto-generated S3 bucket.

KNOWN ISSUES:
  - Removing AZs during stack modification can fail to delete public subnets related to ALB ENIs.
    ---No workaround known, manually delete the ALB.

  - When using a domain, a hosted zone is required to already exist and the stack must be deployed to us-east-1. These are the only current dependencies because domains purchased outside of Route 53 require advance notice of name server configurations.
    ---No workaround, create the hosted zone before stack deployment.

  - A common limit that can halt deployment are Elastic IPs. By default, every account has a limit of 5 EIPs per region.
    ---Workaround 1: Request a service quota increase before deployment.
    ---Workaround 2: Deploy fewer NAT Gateways.
    ---Planned Resolution: Construct a Lambda function to check if deployment will result in a service quota violation, and if so, request the increase via the AWS API.
    
PLANNED IMPROVEMENTS:
  - More Functionality:
    Add resources for Transit Gateway demos.
    Add Lambda demos.
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
    Add LB functionality when using only one AZ.
    Add VPC Flow Logs.
    Add other CloudWatch Resources.
    Add ElasiCache Resources.
    Automatically personalize the index.html page using AWS Lambda.
  
  - More Validation:
    Add an AllowedPattern for OwnedDomainName.
    Add an AllowedPattern for OwnedHostedZoneId.
    Check if the requested AZ count exceeds the region AZ count.

  - Transition from Deprecated Functionality:
    Remove ForwardedValues from CloudFront resources for CachePolicyId.

  - Security Improvements:
    Tighten the S3 Endpoint Policy.
    Add WAF.

  - Remove Manual Processes:
    Automatically empty the S3 bucket on stack deletion.
    Automatically delete the ACM DNS validation Route 53 record on stack deletion.
    Automatically unpack static website resources into the S3 bucket with a Lambda function.

  - Remove Redundancy:
    Consolidate CloudFront Distributions.
    
RELEASE NOTES:
  - Version 1.1, 29 June 2021:
    Bug Fix where lb-cache subdomain was unusable.
    Added Cloud9 Instance deployment.
  - Version 1.0, 22 June 2021:
    Initial Release.
