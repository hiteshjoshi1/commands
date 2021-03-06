# Elastic File System- AWS EFS
  -- Under Storage

- Great for sharing files between multiple Ec2 servers. This is basically a file system that can be shared between compute instances(ec2). It can be mounted and both instances can access it.

- Storage grows and Shrinks automatically
- Great for file servers.
- Pay as we go , no pre provisioning required.
- can support 1000 of concurrent NFS connections.
- Compatible with NFS 4.0 and NFS 4.1
- compatible with Linux based AMIs, does not work for windows as of now.
- Create an EFS volume >> create mount points for the EFS volume in a VPC.
- An EFS volume can attach to only one VPC at a time.

![Screenshot 2020-07-05 at 4 04 07 PM](https://user-images.githubusercontent.com/5917216/86528361-ccb7ce00-bed9-11ea-8508-6ebfc3812b3c.png)


Example, 
- A website can be stored on an EFS   /var/www
and are mounted to multiple Ec2 instances.

"
You have created a file system. You can mount your file system from an EC2 instance with an NFSv4.1 client installed. You can also mount your file system from an on-premises server over an AWS Direct Connect or AWS VPN connection. Click here for EC2 mount instructions, and here for on-premises mount instructions.
"

Update OS - Install Apache - Install Amazon efs utils for mounting EFS -

```
#!/bin/bash
yum update -y
yum install httpd -y
service httpd start
chkconfig httpd on
yum install -y amazon-efs-utils
```

Notes -

- EFS can be created with Encryption - uses NFSv4(Network File System)

- A EFS can be mounted to multiple EC2 Instances

- The amazon-efs-utils allows mounting of EFS to Ec2 Instances.

- If the EFS is created in the dafault EC2 Group, make sure the EC2 instances also are using the same security group.

- For mounting with TLS, There has to be an Inbound NFS Rule in the Security Group(Port 2049) allowing connections from EC2 Instances Security Group.

- EFS with Security group A should have an inbound Rule in A to allow NFS connections from Security group B which is the Security Group of All EC2 Instances.

Mount an EFS file system on /var/www/html directory of apache -
run this command from www folder 

```
sudo mount -t efs -o tls fs-f9af20b8:/ /var/www/html
```
where var/www/html is the mount point.


### FSx for windows server
A managed windows file server that runs on Windows Server Message block(SMB) based file services. 
Built on windows file server, it is a fully managed native Microsoft windows file system.  
Supports Active Dir Users, ACL, groups and security policies along with Distributed File System - DFS namespace and replication.

You cant connect an ec2 on windows with a NFS file system , it has to be FSx file system.
### FSx for Lustre
Fully managed file system for
- compute intensive workloads, example HPC, 
- machine learning,
- media data processing workflows 
- electronic design automation. 
- fsx lustre can store data in amazon s3 as well.

FSX lustre would be used for Millions of IOPS and sub sec latencies. 

# Questions

- Q : An application requires block storage for file updates. The data is 500 GB and must continuously sustain 100 MiB/s of aggregate read/write operations.
Which storage option is appropriate for this application?
- A: Amazon EFS
- E: Speed is faster than EBS.
