# CloudFront - CloudFront is an AWS Content Delivery Network (CDN)
-- Part of Networking - is a global service

So that your media files and other things are cached across the world and user do not have suffer latency downloading them from one location half way around the world.

- Edge Location - Location where content is cached. Edge locations are not just read only. You can write to them.

- Origin - origin of all files that CDN will distribute. An origin could be an - S3 Bucket, EC2, Elastic Load Balancer,Route53.

- Distribution - A distribution is the name given to a CDN which consists of collection of Edge Locations.

Can be used to deliver Dynamic, Static and Streaming content.

Objects are cached in edge locations for TTL(Time To live). You can invalidaten cached content- however you would be charged for cache Invalidation.

### Cloudfront Distribution types -

Distribution Types -
- Web Dsitribution - (for websites)
- RTMP - Media Streaming (adobe)

While creating , it will ask you for Origin(s3, ec2 etc)

You can Restrict Bucket Acess , so that only Cloudfront urls are used to access S3 objects. This is used in Signed URLs case.
There is a radio button for Signed URLs

Objects in the edge locations are cached for the life of TTL (Time to Live).

You can clear cached objects(Cache Invalidate).<b> But that will be charged.</b>

- Restrict Viewer Access in Cloud Front -
  (Use Signed URLs or
  Signed Cookies) ---> Choose whether you want CloudFront to require users to access your content using a signed URL or a signed cookie.

Enable Cloud Front Enable and use as -

http://<Your CLoud front URL>/<Object in S3>

Select a Cloud Front and click Distribution Settings

You can Invalidate objects. -- In case some wrong data is published. Invalidate it. Invalidate objects, directories or everything in CDN.

### Snowball Data Storage

Used for  Import to S3, Export from S3
- Snowball
- Snowball Edge (100 TB , comes with compute and storage)
- SnowMobile (100 Peta bytes)

## Storage Gateway

Storage Gateway supports three key hybrid cloud use cases – 
1. Move backups and archives to the cloud
2. Reduce on-premises storage with cloud-backed file shares
3. Provide on-premises applications low latency access to data stored in AWS.
Works with 3 main Storage protocols - NFS, SMB and iSCSI. 
Storage gateway natively integrates with S3, AWS IAM, and AMS KMS for encrypting data at Rest, Can also monitor using Cloudwatch and log using Cloud Trail.

Available as Virtual Machine [VmWare WSXi or Microsodt Hyper- V] or phsyical device.

Install the gateway --> associate it with your AWS a/c

## Storage gateway types

Storage gateways are of 3 main types - 
1. File Gateway (NFS or SMB)
2. Volume Gateway(iSCSI - Internet Small Computer System Interface)
3. Tape Gateway (VTL) - Virtual Tape Library

### 1.File Gateway

The File Gateway enables you to store and retrieve objects in Amazon S3 using file protocols such as Network File System (NFS) and Server Message Block (SMB). Objects written through File Gateway can be directly accessed in S3.
Your applications read and write files and directories over NFS or SMB, interfacing to the gateway as a file server. In turn, the gateway translates these file operations into object requests on your S3 buckets.

### 2.Volume Gateway
- Provides iSCSI connectivity - Internet Small Computer System Interface.
Data on the volumes is stored in Amazon S3 and you can take point in time copies of volumes which are stored in AWS as Amazon EBS snapshots. 
You can also take copies of volumes and manage their retention using AWS Backup. 
Data written in the volumes can be asynchronously backed up as point in time snapshots of your volumes and stored as EBS Snapshots.
Snapshots are incremental snapshots that only capture changed blocks, the snapshot storage is also compressed to minimize your storage charges.

#### Volume Gateway Types:
1. Stored Mode
2. Cached MOde
#### Stored Mode -
In the stored mode, your primary data is stored locally and your entire dataset is available for low-latency access while asynchronously backed up to AWS.

#### Cached Volumes-
In the cached mode, your primary data is written to S3, while retaining your frequently accessed data locally in a cache for low-latency access.

### 3.Tape Gateway -
The Tape Gateway provides your backup application with an iSCSI virtual tape library (VTL) interface.
Virtual tapes are stored in Amazon S3 and can be archived to Amazon S3 Glacier or Amazon S3 Glacier Deep Archive.


# Questions-
Q: A legacy application needs to interact with local storage using iSCSI. A team needs to design a reliable storage solution to provision all new storage on AWS.
Which storage solution meets the legacy application requirements?
A: AWS Storage Gateway in stored mode for the legacy application storage to write data to Amazon S3.
Explanation- As all new storage has to be provisoned on AWS. AWS Stored Volumes is our best option.



