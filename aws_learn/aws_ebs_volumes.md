# EBS - Elastic Block Store

Virtual Hardisk on the cloud provided with EC2.

## EBS Types -

- General purpose SSD - For most use cases [gp2] 16000 iops
- Provisioned IOPS - Highest performing SSDs examplefor Databases [io1] 64000 ips
- Throughput optimized HDD - Big data and Data warehouses [st1] 500 Iops
- Cold HDD - File Servers [sc1] 250 Iops
- EBS Magenetic Drive - Infrequently accessed data[Standard] 40-200 IOps

Underlined is the Api name


Volumes are hard disks

Snapshots are backups of Volumes

Volume -->Create Snapshot--> Create image from Snapshit --> Volume in new region

however, you can create an AMI from both volumes or snapshot.

### Migration -
AMI can be moved to move EC2 between Availability Zones(us east 1a, us east 1 b), And
AMI can be moved used to move EC2 between Regions  (us east, Singapore)


When you Terminate EC2 Instance, root device volume will also be deleted. Any other Volumes will not be deleted.

Snapshots are deleted, whereas AMI have to be de-registered.



AMI 's can be selected based on
1.Region
2.OS
3.Architecture (32 bit or 64 bit)
4.Launch Permissions ???
5.Storage for Root device(Root Device Volume)-
  - Instance Store(Ephemeral Storage)
  - EBS Backed Volumes

## AMI Types
- EBS (Amazon EBS Volume created from an Amazon EBS Snapshot)
- Instance Stores (Instance Store Volume created from a template stored in Amazon S3) - Ephemeral Storage

When  Instance Stores is Stopped we loose all data, hence Ephemeral Storage.


## Encrypted Root Device Volumes and Snapshots -
Steps -
- Create an Ec2 Instance, It is Volume would not be encrypted by default
- Create a Snapshot from it
- Copy that Snapshot , select encryption
- Using this encrypted Snapshot to create an Image(AMI)
- Launch the Image(AMI) as Ec2 instance, which will now have Encrypted Volumes.





