# AWS Cloud Formation
AWS CloudFormation provides a common language for you to model and provision AWS and third party application resources in your cloud environment.
AWS CloudFormation allows you to use programming languages or a simple text file to model and provision, in an automated and secure manner,
all the resources needed for your applications across all regions and accounts. This gives you a single source of truth for your AWS and third party resources. 

# AWS Service catalogue
AWS Service Catalog allows organizations to create and manage catalogs of IT services that are approved for use on AWS. These IT services can include everything from virtual machine images, servers, software, and databases to complete multi-tier application architectures. AWS Service Catalog allows you to centrally manage commonly deployed IT services.

# Cloud Watch
- Monitor applications by collecting logs, metrics and events.
- Visualizes data into dashboards.
- You can setup alarms based on metric values and add actions like notifications of anomalous behavior and even trigger automated auto scaling actions.
- Upto 1 sec metric collection
- 15 month data retention

# AWS System Manager
Aggregates AWS services into groups,  view aggregated operational data on group level.
ITSM tools with scripting to act on group of AWS resources.

# AWS Cloud Trail
Who did what in the AWS account.
Log, monitor and retain activity related to actions across your AWS infrastructure
- delivers events to cloudtrail console, Amazon s3 or to Cloudwatch Logs


# AWS Opsworks
Managed instances of Chef and Puppet.

# AWS config
- Monitor and record configuration changes to Aws resources.
- Allows you to continuously audit and assess the overall compliance of your AWS resource configurations with your organization’s policies and guidelines.
- Multi account multi region data aggregation in AWS cofig, you can view compliance across your enterprise and flag non compliant accounts.
- You can use AWS Config as your framework for creating and deploying governance and compliance rules across your AWS accounts and regions.
You can codify your compliance requirements as AWS Config rules and author remediation actions using AWS Systems Manager 

# AWS Trusted advisor
Can analyze your cloud resources and advice best usage and security practices.

# AWS Cloud Front - Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to 
customers globally with low latency, high transfer speeds, all within a developer-friendly environment.
CloudFront works seamlessly with services including AWS Shield for DDoS mitigation, Amazon S3, Elastic Load Balancing or Amazon EC2 as origins for your applications,
and Lambda@Edge to run custom code closer to customers’ users and to customize the user experience.
Lastly, if you use AWS origins such as Amazon S3, Amazon EC2 or Elastic Load Balancing, you don’t pay for any data transferred between these services and CloudFront.
