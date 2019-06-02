# AWS Notes

IAM
S3
Buckets

## Creating buckets in S3

    By default  objects in Buckets are not public.

## Lifecycle Rules for S3 Bucket objects

    Automate movement of object between storage tiers.
    Can be used in conjuction with versioning - that means version of documents can also be moved between  Storage tiers using Lifecycle Rules.

    Bucket> Management> Lifecycle Rules

### Bucket Cross Region replication

    Cross Region Replication requires versioning enabled

Can replicate entire buckets using Replication
or can replicate specific tags or Prefix

\*\*\* Only new changes will be replicated, that is any object that was alreay there before replication was turned On - would not be replicated

\*\*\* Delete marker is not replicated
Deleting individual versions would also not be replicated

### S3 transfer acceleration

Upload a file to edge location

Which will then moved to S3 bucket. This is faster

## CloudFront - CloudFront is AWS CDN

Edge Location - Location where content is cached.

### Origin - origin of all files that CDN will distribute. Example, S3 Bucket, EC2, Elastic Load Balancer,Route53.

### Distribution - Cloud Distribution types -

A distribution is the name given to a CDN which consists of collection of Edge Locations.
Distribution Types

- Web Dsitribution
- RTMP - Media Streaming

Objects in the edge locations are cached for the life of TTL (Time to Live). You can clear cached objects(Cache Invalidate). But that will be charged.

Restrict Viewer Access
(Use Signed URLs or
Signed Cookies) ---> Choose whether you want CloudFront to require users to access your content using a signed URL or a signed cookie.

Cloud Front Enable -

CLoud URL/Object/s in S3.

Select a Cloud Front and click Distribution Settings

Then you can Invalidate objects.
