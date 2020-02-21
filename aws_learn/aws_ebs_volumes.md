# EBS - Elastic Block Store
it is under EC2--> Volumes
EBS will be in same Availability Instance as EC2.

Virtual Hardisk on the cloud provided with EC2. Each EBS is automatically replicated within its Availability zones.

## EBS Types -

- General purpose SSD(gp2) - For most use cases --> 16000 iops per volume
- Provisioned IOPS SSD(io1) - Highest performing SSDs --> for Databases --> 64000 ips per volume
- Throughput optimized HDD (st1) - Big data and Data warehouses --> 500 Iops per volume
- Cold HDD(sc1) - File Servers --> 250 Iops per volume
- EBS Magenetic Drive - Infrequently accessed data[Standard] --> 40-200 IOps per volume

EBS types can be changed on the fly, including the size. Volumes will always be in the same avaialibility zones as in EC2.


Snapshots are point in time backups of Volumes. They are used to move volumes from 1 AZ to other.

Volume -->Create Snapshot--> Create image from Snapshot --> Volume in new region

however, you can create an AMI from both volumes or snapshot.

### Migration - Using Snapshots
AMI can be moved to move EC2 between Availability Zones(us east 1a, us east 1 b), And
AMI can be moved used to move EC2 between Regions  (us east, Singapore)

Snapshots ---> Create image from Snapshot 

Virtualization types while creating Images from Snapshot -
- Paravirtual(PV)
= Hardware Virtual Machine Virtualization(HVM) - preferred

Once the Image(AMI- Amazon Machine Image) is created, it can be used to launch Ec2 instances. Move AMI to another region and then create EC2 instances from it.

Snapshots are deleted, whereas AMI have to be de-registered.
Snapshots are stored in S3.Snapshots are incremental - only changes will be backed up.

When you Terminate EC2 Instance, root device volume will also be deleted. Any other Volumes(non-root volumes) will not be deleted.


[AMI 's can be selected based on] ~
1.Region
2.OS
3.Architecture (32 bit or 64 bit)
4.Launch Permissions - ??
5.Storage for Root device(Root Device Volume)-
  - Instance Store(Ephemeral Storage) - Root device is created from template stored in S3, cannot stop such an Ec2 instance, only restart, terminate.
  - EBS Backed Volumes - Root device volume is created from snapshot.

  

## AMI Types
- EBS (Amazon EBS Volume created from an Amazon EBS Snapshot)
- Instance Stores (Instance Store Volume created from a template stored in Amazon S3) - Ephemeral Storage

When  Instance Stores is Stopped we loose all data, hence Ephemeral Storage.


## Encrypted Root Device Volumes and Snapshots -
Steps -
- Create an Ec2 Instance, It is Volume would not be encrypted by default
- Create a Snapshot of the unencrypted root device volume.
- Create a Copy of that Snapshot , select encryption option(Encrypt this snapshot)
- Create an AMI from the Encrypted Snapshot.
- Launch the Image(AMI) as an Ec2 instance, which will now have Encrypted Volumes.


You can share snapshots but inly if they are not unencrypted.





