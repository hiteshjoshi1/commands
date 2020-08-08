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

