# S3 - Simple Storage Service


An AWS Account can have 100 S3 buckets by default in a account. All buckets by default are private.

Bucket policies and ACL. Can capture Access Logs of an S3.

S3 - is a universal namespace, so Bucket Name has to be unique.


S3 has 99.99%  availability

S3 is a filestore which is Object Based whereas EBS is Block based. S3 not suitable for storing Operating System.

### Consistency Model for S3 

Read after Write consistency for PUTS of New Objects
Eventual consistency for overwrite PUTS and Deletes

### Storage Classes in S3 

- S3 Standard {can sustain loss of 2 facilities concurrently} -- Costliest - 99.99%
- S3- IA (S3 Infrequently Accessed - lower fee than s3 but you are charged retrieval fee) - use it when the data kept is  infrequently accessed.
- S3 One zone -IA (Only in one zone - multi zone resilence not required). Availaibility is 99.50% whereas for S3-IA it is 99.99
- S3 Intelligent Tiering - Moves data to most cost effective access Tier
- S3 Glacier - data archiving, retrieval time from Mins to Hours
- S3 Glacier - Deep Archive [retrieval 12 hours]
- S3 - RRS - Reduced Redundancy Storage (Deprecated) has 99.99% availability and durability. But fault tolereance is 1, instead of 2 in S3       Standard and S3 - IA. RRS is being deprecated. It is similiar to S3 - One zone -IA.


OneZone-IA is the recommended storage for when you want cheaper storage for infrequently accessed objects. It has the same durability but less availability. There can be cost implications if you use it frequently or use it for short lived storage. Glacier is cheaper, but has a long retrieval time. RRS has effectively been deprecated. It still exists but is not a service that AWS want to sell anymore.

Full S3 is quite expensive at around $0.023 per GB for the lowest band. S3 standard IA is $0.0125 per GB, S3 One-Zone-IA is $0.01 per GB, and Legacy S3-RRS is around $0.024 per GB for the lowest band. Of the offered solutions SS3 One-Zone-IA is the cheapest suitable option. Glacier cannot be considered as it is not intended for direct access, however it comes in at around $0.004 per GB. RRS is being deprecated. No such thing as Provisioned IOPS.


### Encryption Types in S3
- Encryption in Transit is achieved by(SSL/TLS)
- Encrption at rest can be managed by -
   1. S3 Managed Keys - SSE-S3 (Server Side encryption with AWS managed keys with AES - 256)
   2. SSE - KMS (Server Side Encryption - Key Management Service)
   3. SSE with customer provided keys(SSE- C)
   4. Client side encryption

### Versioning
- When versioning enabled on a bucket, it store different versions of files.
- When you upload a new version of a file, if the version1 is public, version 2 will by default be not public(Version 1 if public will stay public).
- Versioining will even store delete version(delete marker).
- Versioning has MFA(multi Factor auth) delete facility.


### S3 Lifecycle Rules

- Automate S3 objects lifecycle, example movement of object in S3 between storage tiers or delete/expire objects.
- Can be used in conjuction with versioning -> that means version of documents can also be moved between Storage tiers using Lifecycle Rules.

Bucket> Management> Lifecycle Rules

### S3 Cross Region replication

 **Cross Region Replication requires versioning enabled

Can replicate entire buckets using Replication or can replicate specific tags or Prefix


Notes - 
1. Only new objects will be replicated, that is any object that was already there before replication was turned on would not be replicated

2. Delete marker is not replicated with cross region replication.
3. Deleting individual versions would also not be replicated

### S3 transfer acceleration

Utilizes Cloud front edge location to upload files---> Backbone ---> S3 Bucket

Upload a file to edge location. Which will then moved to S3 bucket using AWS backbone network. This is faster then direct upload to S3.
So you are region1 and your user is half way across the world you would benefit from Transfer acceleration when he uploads a file.

Questions --

One of your users is trying to upload a 7.5GB file to S3. However, they keep getting the following error message: "Your proposed upload exceeds the maximum allowed object size.". What solution to this problem does AWS recommend?
Answer - Design your application to use multipart upload API for all objects.


