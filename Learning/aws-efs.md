# AWS EFS - Elastic File System

Grows and Shrinks automaticallu

Great for file servers

Great for sharing files between multiple Ec2 servers.

A website can be stored on an EFS
/var/www
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

```
sudo mount -t efs -o tls fs-f9af20b8:/ /var/www/html
```