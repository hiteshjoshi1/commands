# AWS RDS -

Multi AZ(DNS pointing to primary but if primary fails, rolls over to secondary) and read replicas(copies of primary for reads).

## Supported Relational Dbs ->
- Microsoft Sql Server
- Oracle
- Mysql Server
- PostgreSql
- Amazon Aurora
- MariaDb

**NOSql DBS** ->
Dynamo Db

**OLAP (Online Analytical Processing, Data Warehousing)** -->
Amazon Redshift

**In Memory Cache** -->
ElasticCache

**Relational Database options** -->
Multi AZ(Availability Zones) -> For disaster recovery. Failover detected automatically and remediated.
Read Replicas -> For Performance, no automatic failvers.- 5 copies/replicas

OLTP - Order number  11101--> get data and do something(Sql, Mysql, etc)

OLAP --> complex query, example profit of a product based by region in multi years.(Redshift)

## Create an RDS Instance

Create Relational database and connect it with the Ec2 instaces.

AWS instances are n ot serverless. They are physical Ec2 machines but we(end user) cannot access them.
SSH - not allowed.
AWS Aurora however can be serverless.

## Backups-

The restored version of database from a backup would be a brand new RDS instance with a new endpoint.

- Automated Backups
- Database Snapshots

**Automated Backups** -
Full day snapshots and store the transaction logs as well. Allows the point in time delivery down to second within the retention period.
Are enabled by default.
Backups are stored in S3.You get free storage equal to the size of your database.

Backups is done within a defined window, during the window storage I/O may be suspended and we might experience increased latency.

**Database BackUps**-
Done manually by us.(Unlike Automated backups).
They are stored even after the original RDS instances are deleted.

Encryption is done using Amazon KMS (Amazon Key Management Service).

### Encryption is available for -

- SQl Server
- Oracle
- MySql Server
- PostgresSql
- MariaDb
- Aurora

Once encryption is enabled,data stored in the underlying instances is encrypted in snapshots , backups etc.

**Multi - AZ Backup**
Used for Disaster Recovery

Modify Db instance-->Multi AZ deployment

RDS is backed up in different Availability zones. Data is synchronously replicated to other RDS in a different Availaibility endpoints. Provides automatic disaster failure recovery. No need to change the URL, amazon will change the IP internally to the AZ backup internally in case of a failover.

### Multi AZ backup is available for-

- SQl Server
- Oracle
- MySql Server
- PostgresSql
- MariaDb

**Read Replicas**

For Performance improvement.
They need to have backups turned ON. So TUrn on Deployment first before you can enable Read replicas.
They can be Multi AZ or be in Different Region altogether.
Ec2 instances can READ from multiple replicas. But they all write to one primary which is then asynchronously replicated to the Read replicas.

How do you increase database performance?

- By using Read replicas
- By using Cache for heavily used data.

### Read replicas are Availiable for -

- MySql Server
- PostgresSql
- MariaDb
- Aurora

**Must have automatic backups turned on in order to have a read replica.**
You can 5 replica copies of any database
You can have replicas of replicas.
Each replica will have its own DNS endpoint.
You can have replicas that have Multi-AZ.
You can have Read replicas of multi AZ source databases
Read replicas can be promoted to be their own databases(be their own Master) - this breaks this replication.
You can have read replica in a completely seprate region.


### AWS Data Migration Services
- DMS allows you to migrate database from on prem to AWS, AWS one db to AWS another db, AWS to on-prem, other cloud providers(azure) to AWS etc.
- You can do homogeneous migrations(Same src and destination db type) or hetrogeneous migrations(Source and destination db type are different)
- For hetrogeneous migrations we will need a schema conversion tool.

- Sources - Oracle, Microsoft SQL server, MySQL, MariaDB, PostgresSQL, SAP, Mongodb, Db2, Azure SQL databases, Amazon RDS(Inluding aurora) and even Amazon s3
- Destination - Oracle, Microsoft SQL server, MySQL, MariaDB, PostgresSQL, SAP, RDS, Redshift, DyanamoDb, S3, Elastic Search, Kinesis data streams, DocumentDB


