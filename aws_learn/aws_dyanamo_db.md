# Dynamo DB
NO SQL database solution - FULL managed service
- sub second latency
- Stored on SSD Storage
- is Serverless
- eventual consitency reads(default) - reads after 1 sec after write
- can have strongly consistent reads - read immediately after writes
- Spread across 3 geographically distinct data centres
- makes it fit for mobile, web, gaming , ad-tech, IOT etc.

### Read Models -

- Eventual Consistent reads(default)
- Strongly Consistent reads

Eventually consistent reads - roughly 1 sec consistent
Strongly Consistent Reads - less than 1 sec consistent

### DynamoDb Accelerator (DAX)
- It is a fully managed, highly available, in- memory cache. 
- It can also act a write through cache.
- 10x performance improvement
- reduces request time from millisec to microsec
- devlopers do not manage caching logic 
- compatible with dynamodb api calls

### Transactions in DynamoDb
Two underlying reads or writes - one to read and write - prepare/commit
Transactions can act on 25 items or 4MB of data

### On demand capacity
- pay per request pricing
- bal cost and performance, no min capacity, no charge for read or writes only charge for storage and backups
- But the cost is higher per request than provisioned capacity
- so use when the load is not predicatable, ex new product launches

### On demand backup and restore

- full backups at any time
- zero impact on db performance or availability
- consistent within seconds and retained till deleted 
- operates within the same region as the source table - so backups and restores cannot be done across regions

### Point in time recovery
- Restores to any point in the last 35 days
- not enabled by default
- Latest restorable point - 5 mins in the past

### Dynamodb streams

- Time ordered sequence of item level changes in a table
- Stored for 24 hours
- inserts, updates and deletes that happened in the last 24 hrs
- stream records - every shard has stream which has stream records, a stream record has stream number
- can combine streams with lambda function to have stored procedure like functionality

### Amazon Global Tables
It is managed multi master , muli -region reploication
- built on dynamo db streams
- multi region redundancy for HA and DR
- no application rewrites required
- replication latency is under 1 sec across regions.

### Database migrations services
not necessarily related to dyanamodb
it is a migration application.

### Security dynamodb

- Encrypted at rest using KMS
- Site to Site VPN in case you have on prem
- Direct Connect (DX)
- IAM policies and roles to Dynamo db tables 
- Fine grained access - IAM policy that allows users access only to certain areas of dynamo db
- VPC endpoints -- to enable ec2 instances in your vpc to use their private ip address withut any exposure to internet
- Cloudwatch and Cloudtrail


