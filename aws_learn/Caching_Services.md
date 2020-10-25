## Caching Services in AWS

- CloudFront (Caches origin- S3 bucket,Ec2, Application Load balancer, Route53)
- API Gateway (Cloudfront - api gateway- lambda )
- Elastic Cache - Memcached and Redis
- DynamoDb Accelerator (DAX) - Caching layer in Dynamo DB.

Cache in front means lower latency.
Caching is a balancing act between up- to date information and latency.
