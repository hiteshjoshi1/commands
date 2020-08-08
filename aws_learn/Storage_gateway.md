# AWS Storage gateway
AWS Storage Gateway is a hybrid cloud storage service that gives you on-premises access to virtually unlimited cloud storage. It is used for 
moving backups to the cloud, using on-premises file shares backed by cloud storage, and providing low latency access to data in AWS for on-premises applications.

## Storage Gateway

Storage Gateway supports three key hybrid cloud use cases – 
1. Move backups and archives to the cloud
2. Reduce on-premises storage with cloud-backed file shares
3. Provide on-premises applications low latency access to data stored in AWS.

### Works with 3 main Storage protocols - NFS, SMB and iSCSI. 
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



