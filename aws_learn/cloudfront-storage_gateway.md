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
