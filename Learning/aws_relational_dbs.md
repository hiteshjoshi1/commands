#AWS RDS -

**Supported Relational Dbs** ->
Microsoft Sql Server
Oracle
Mysql Server
PostgreSql
Amazon Aurora
MariaDb

**NOSql DBS** ->
Dynamo Db

**OLAP (Online Analytical Processing, Data Warehousing)** -->
Amazon Redshift

**In Memory Cache** -->
ElasticCache

**Relational Database options** -->
Multi AZ(Availability Zones) -> For disaster recovery, Failover detected and remediated
Read Replicas -> For Performance, no automatic failvers.

## Create an RDS Instance

Create Relational database and connect it with the Ec2 instaces.

AWS instances are n ot serverless. They are physical Ec2 machines but we(end user) cannot access them.
SSH - not allowed. AWS Aurora however can be serverless.
