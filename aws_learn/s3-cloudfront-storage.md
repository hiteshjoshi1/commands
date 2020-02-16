# AWS Notes

## Region 
A region is a geographical area with different availability zones. Each region consists of two or more availability zones.
It consists of independent collection of AWS computing resources.

## Availaibilty zones (AZ)
Distinct locations within an AWS region that are engineered to be fault tolerant.

### Elastic Beanstalk vs Cloud Formation

Elastic BeanStalk automatically handles deployment capacity privisioning, load balancing, auto scaling to application health monitoring based on the code you upload to it.

Cloud Formation is an automated provisoning engine designed to deploy entire cloud environments via JSON script.


### kinesis - 
For collecting large amount of data streamed from various sources

### Cloud Trail
To creeate Audit Logs of who provisoned what instances in AWS.

### Ops works
A configuration management service that enable your system administarators to configure and manage your web applications using chef.

### Elastic Transcoder 
Service  to convert media files to different formats to suit different devices.


## S3 et al

CAN have 100 S3 buckets by default in an account.

IAM - IAM (Identity Access Management) is universal and not specific to a region.
S3 - is a universal namespace
Buckets - so Bucket Name has to be unique.


S3 has 99.99%  availability


S3 is filestore which is file Based whereas EBS is Block based.

### Consistency in S3 -->

Read after Write consistency for PUTS of New Objects
Eventual consistency for overwrite PUTS and Deletes

### S3 classes of Storage --

- S3 Standard {can sustain loss of 2 facilities concurrently}
- S3- IA (S3 Infrequently Accessed - lower fee than s3 but you are charged retrieval fee)
- S3 - RRS - Reduced Redundancy Storage has 99.99% availability and durability. But fault tolereance is 1, instead of 2 in S3       Standard and S3 - IA. RRS is being deprecated.
- S3 One zone -IA (Only in one zone - multi zone resilence not required). Availaibility is 99.50% whereas for S3-IA it is 99.99
- S3 Intelligent Tiering - Moves data to most cost effective access Tier
- S3 Glacier - data archiving, retrieval time from Mins to Hours
- S3 Glacier - Deep Archive [12 hours]


OneZone-IA is the recommended storage for when you want cheaper storage for infrequently accessed objects. It has the same durability but less availability. There can be cost implications if you use it frequently or use it for short lived storage. Glacier is cheaper, but has a long retrieval time. RRS has effectively been deprecated. It still exists but is not a service that AWS want to sell anymore.

Full S3 is quite expensive at around $0.023 per GB for the lowest band. S3 standard IA is $0.0125 per GB, S3 One-Zone-IA is $0.01 per GB, and Legacy S3-RRS is around $0.024 per GB for the lowest band. Of the offered solutions SS3 One-Zone-IA is the cheapest suitable option. Glacier cannot be considered as it is not intended for direct access, however it comes in at around $0.004 per GB. RRS is being deprecated. No such thing as Provisioned IOPS.


### Encryption in Transit is achieved by

- S3 Managed Keys - SSE-S3
- SSE- KMS (Key Management Service)
- SSE with customer provided keys(SSE-C)
- Client side encryption

## Creating buckets in S3

    By default  objects in Buckets are not public.

## Lifecycle Rules for S3 Bucket objects

    Automate movement of object in S3 between storage tiers.
    Can be used in conjuction with versioning - that means version of documents can also be moved between  Storage tiers using Lifecycle Rules.

    Bucket> Management> Lifecycle Rules

### Bucket Cross Region replication

- Cross Region Replication requires versioning enabled

Can replicate entire buckets using Replication
or can replicate specific tags or Prefix

\*\*\* Only new changes will be replicated, that is any object that was alreay there before replication was turned On - would not be replicated

\*\*\* Delete marker is not replicated
Deleting individual versions would also not be replicated

### S3 transfer acceleration

Upload a file to edge location. Which will then moved to S3 bucket. This is faster
So you are region1 and your user is half way across the world you would benefit from Transfer acceleration when he uploads a file.

Questions --

One of your users is trying to upload a 7.5GB file to S3. However, they keep getting the following error message: "Your proposed upload exceeds the maximum allowed object size.". What solution to this problem does AWS recommend?
Answer - Design your application to use multipart upload API for all objects.


## CloudFront - CloudFront is an AWS CDN

So that your media files and other things are cached across the world and user do not have suffer latency downloading them from one location half way around the world.

 - Edge Location - Location where content is cached. Edge locations are not just read only. You can write to them.

- Origin - origin of all files that CDN will distribute - The origin could be an - S3 Bucket, EC2, Elastic Load Balancer,Route53.

- Distribution - A collection of edge locations.



### Cloud Distribution types -

A distribution is the name given to a CDN which consists of collection of Edge Locations.
Distribution Types

- Web Dsitribution - (for websites)
- RTMP - Media Streaming (adobe)


Objects in the edge locations are cached for the life of TTL (Time to Live).
You can clear cached objects(Cache Invalidate).<b> But that will be charged.</b>

- Restrict Viewer Access in Cloud Front -
  (Use Signed URLs or
  Signed Cookies) ---> Choose whether you want CloudFront to require users to access your content using a signed URL or a signed cookie.

Enable Cloud Front Enable and use as -

http://<Your CLoud front URL>/<Object in S3>

Select a Cloud Front and click Distribution Settings

Then you can Invalidate objects.

### Snowball Data Storage

Import to S3, Export to S3
Snowball
Snowball Edge
SnowMobile

## Storage Gateway

Replicate your on-prem device to AWS cloud.

Available as Virtual Machine [VmWare WSXi or icrosodt Hyper- V]

Install the gateway --> associate it with your AWS a/c

### Storage gateway type ->

- File Gateway (NFS)
- Volume Gateway
  Types - - Stored Volume - Cached Volumes
- Tape Gateway (VTL) - Virtual Tape Library

### File Gateway

For Flat Files - Stored directly on S3
File are stored in S3 and accessed through a network file system (NFS) mount point.
All user metadata, permissions and timestamps are stored in user metadata of the object stored in the file.

### Volume Gateway

Back up your data disk drives using the iSCI block protocol.
Data written in the volumes can be backed up as point in time snapshots of your volumes and stored as EBS Snapshots

Snapshots are incremental snapshots that only capture changed blocks, the snapshot storage is also compressed to minimize your storage charges.

### Stored Volumes -

Entire dataset is kept locally(local SAN) and asychronously backed up to S3.

### Cached Volumes-

Only recently used data is stored in on prem storage gateway.
The entire dataset actually resides in S3, however the recently used data is cached in the local storage Gateway.

Tape Gateway -
Lets you archive your data to AWS cloud.
VTL interface allows existing Tape data to S3.
