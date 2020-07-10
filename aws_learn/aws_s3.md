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
   
   ----
 1. SSE-S3 requires that Amazon S3 manage the data and the encryption keys. For more information about SSE-S3, see Protecting Data Using Server-Side Encryption with Amazon S3-Managed Encryption Keys (SSE-S3).

2. SSE-C requires that you manage the encryption key. For more information about SSE-C, see Protecting Data Using Server-Side Encryption with Customer-Provided Encryption Keys (SSE-C).

3. SSE-KMS requires that AWS manage the data key but you manage the customer master key (CMK) in AWS KMS.

The remainder of this topic discusses how to protect data by using server-side encryption with AWS KMS-managed keys (SS
   

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


### 3 ways to share s3  bucket across accounts -
1. Using Bucket policies and IAM(entire bucket, cant lockdown individual objects). -- Programmatic access only
2. Using Bucket ACL and IAM(works on individual objects) -- Programmatic access only

3. Cross Account IAM roles- programmatic and console access
This is how Type 3 is done.
    -LOGIN TO Master Acc, then 
    --> Cross IAM role --> Select Type of Trusted entity  - choose Another AWS account - Provide Other aws accounts accountID
    --> Attach policy to this role --> S3FullAccess --> Give role a name and Create Role 
    
    This will give out a link.
 4. Sign in with another Aws account. 
       -->Create another user (cant use root account)
       -->Create Admin grp, with Administrator access policy
   Sign with the newly created User
   --> Switch Role / or Just paste the link in Step 3.
 5. This switched account can now view S3.  

## Questions --

- Q: One of your users is trying to upload a 7.5GB file to S3. However, they keep getting the following error message: "Your proposed upload exceeds the maximum allowed object size.". What solution to this problem does AWS recommend?
- A: - Design your application to use multipart upload API for all objects.

- Q: A company is evaluating Amazon S3 as a data storage solution for their daily analyst reports. The company has implemented stringent requirements concerning the security of the data at rest. Specifically, the CISO asked for the use of envelope encryption with separate permissions for the use of an envelope key, automated rotation of the encryption keys, and visibility into when an encryption key was used and by whom.
Which steps should a Solutions Architect take to satisfy the security requirements requested by the CISO?
- A:  Create an Amazon S3 bucket to store the reports and use Server-Side Encryption with AWS KMS-Managed Keys (SSE-KMS).




