# EC2 - Elastic Compute cloud

Pricing philosophy(Not needed for exam)

- Pay as you go and pay for what you use
- Pay less as you use more
- Pay even less when you reserve capacity

## EC2 Pricing Models -

- On Demand
- Reserved (1 yr or 3 yr contracts, predictable work loads)
    1. Standard Reserved instances
    2. Convertible reserved instances (can change instance types)
    3. Scheduled reserve instances
- Spot - Price moves around, excess capacity
- Dedicated Hosts



### On Demand -

Low cost, no upfront fee and no long term commitment
Good for 1st time amazon AWS users
Good for short term, spiky or unpredicatble workloads that cannot be interrupted

### Reserved Pricing -

Used for predictable usage
Upfront payments lead to cheaper pricing, 1 or 3 years instances

    - Standard Reserved Instances -
    75% cheaper, more you pay upfront, longer the contract, higher the discount.
    You cant convert one reserved instances to other instances.

    - Convertible Reserved Instances -
    You can convert one reserved instances to another.

    - Scheduled Reserved Instances -
    Available within the time windows you reserve.
    
    Can a reserved instance be moved from 1 region to another? NO
  Depending on you type of RI you can You can modify the AZ, scope, network platform, or instance size (within the same instance type), but not Region. In some circumstances you can sell RIs, but only if you have a US bank account.



### Spot Pricing - Might use this for own websites

AWS selling off its unused inventory.
Applications that have flexible start and end times.
Applications that are only feasible at very low compute prices.

### Dedidicated Host Pricing

Useful for regulatory requirements which do not allow multi tenant virtualization.
Can be purchased ON -Demand or at Reserved Pricing(Discounted 70% of On Demand).

### EC2 Instance Types - {Not required for Soln Arch Assoc exam}

**FIGHT-DR-MC-PXZ-AU (Fight DR Mc Pxz Australia)

- F FPGA
- I IOps
- G Graphics
- H High Disk Throughput
- T t2 Micro - Cheap General purpose
- D Density
- R RAM
- M Main choice for general purpose apps
- C Compute
- P Graphics (Pics)
- X Extreme memory
- Z Extreme Memory and CPU
- A ARM based workloads
- U Bare metal

You specify what type of EC2 instances.
How much Storage (EBS)  for root device volume? --> this is where the OS gets installed.
**NOTE Root device volume -- can be encrypted. When instance gets deleted, the root device volume will get deleted. Any additional volume wont be get deleted.**

Termination protection is turned off by default.
You also create a pub/ private key pair to connect to your ec2 using SSH.


### EC2 Security -

### Security Group - This is the place where you create inbound and outbound rules for access to Ec2 instances.

Security groups are created for a VPC(Virtual Private Cloud).
Changes to inbound and outbound rules take effect immediately. 
Are stateful - an inbound rule also creates a outbound rule.


KeyPair - Create public private key pair(or use existing) that will allow you to access your instance.(This will be a .pem file)

- You cannot Block individual IPs using Security Groups. Use NACL for that (Network Access Control List).
- No block rules(block any specific IPs) are allowed, by default everything is blocked and rules allow specific access.
- All Inbound traffic is blocked by default and we enable rules to allow access.
- All Outbound traffic is allowed.
- Changes to Rules in Security Group takes place immediately.
- You can add more than one Security Group attached to an Ec2 Instance.


- On an EBS backed instance, when the instance is terminated it will by default delete the root EBS volume. This can be changed so that Volume is not deleted when EC2 instance is terminated.
  (EBS covered later)
- When Adding Storage - Root device volume cannot be encrypted on launch, however if you add new Volumes those can be encrypted. Root device volume is the volume where the Operating System is stored.
  Root device volumes can later be encrypted.

## Practical

Connecting with Pem file (Private key)

1. Get AWS Public IP
2. Go to the folder where Pem is kept in Terminal
3. change the permission of PEM - Read permission only (Not sure why)

```
chmod 400 MYAWSKEYPair.pem
```

4. Then connect using

```
ssh ec2-user@<publicIP> -i MYAWSKEYPair.pem

```

5. Once connected, Update Linux

```
yum update -y
```

6. Install Apache(Webserver)

```
yum install httpd
```

7. Start Apache

```
httpd start
```

8. Put your static website under -
   /var/www/html/

Apache will serve the website at the public IP of AWS EC2.

## Ec2 Placement Groups
Placement grops are recommended for applications that require low network latency, high n/w throughput or both.

- Cluster Placement Group
- Spread Placement Groups
- Partitioned Placement Groups

#### Clustered Placement Groups -
is a Grouping of instances all within an availability zone. When you want EC2 instances as closely a possible.
This cannot span multiple AZ.

#### Spread Placement Group -
Are each placed on distinct underlying Hardware. Reduce to overall business risk.
Spread Placement group can even be in multiple availability zones.
Small number of critical instances that should be kept seprate from each other.
Spread placement groups have a specific limitation that you can only have a maximum of 7 running instances per Availability Zone. 

#### Partitioned Placement Groups
Similiar to Spread Placement group, but can have multiple ec2 instances. Multiple instances in 1 rack and other instances in other rack. All racks have their own network and power source.

Note -
- You cant merge placement groups.
- You cant move an existing instance into a placement group.
- You can create an AMI from your existing instance and then launch the new instance from the AMI into a
placement group.
- AWS recommends homogenous instances in EC2
- only certain type of instances can be in placement group - Compute optimized, GPU, Memory Optmized, Storage optimized,etc
- You can move an existing instance into a Placement group, but the instance has to be in stopped state.This can be done via cli or AWS SDK, not through console yet.
- No charge for creating placement groups.

## EC2 Spot Instances
90% discount compared to on-demand applications.
Decide what is maximum spot price - instance will be provisioned as long as the Spot price is below your maximum spot price.

**Spot Block - 1 to 6 hours... do not terminate even if the spot price goes over maximum spot price.

- not good for databases
- not good for critical jobs
- not good for persistent workloads

Spot instance request -
1. Max price
2. Desired number of instances
3. Instance specs
4. Request type : one time OR persistent (persistent will recreate if the price goes again below max price)
5. Valid from and Valid until

### Spot fleets
collection of spot instances and may be on - demand instances.

#### Spot fleet strategies
1. capacity optimized -- spot instances comes from the pool with optimal capaity for th number of instances launching,
2. lowestPrice -- Spot instances comes from the pool with lowest price (default)
3. diversified -- Spot instances distributes across all pools.
4. instancepoolstocount -- used along with lowest price, spot insrances are distributed across the number of spot instances pools you specify  


## ENI vs ENA vs EF

#### ENI- Elastic Network Interface 
Essentially virtually network card.
Allows
A primary private IPv4 addess from the ipv4 adsress range of the vpc
1 or more sec privare ipv4 address from the ipv4 adsress range of the vpc
1 elastic IP address 
1 public ipv4 address
1 or more ipv6 address
1 or more security group
1 or more MAC address
A source and destination check flag

Where would you use ENI-
- Creating Mgmt n/w
- N/w security appliances in VPC
- Create Dual homed instances with workloads on distinct subnets
- Low budget high availaibility solutions.

#### EN- Enhanced Networking

Uses SR-IOV(Single root I/O Virtualization) to provide high performance n/w for supported instances types. 
Provides Higher I/O performance and lower CPU utilization. Provides better bandwidth. Lower latencies. 
no additional charges but the instance type should support it.
Types of EN - 
- ENA - Elastic Network Adapter (Network speeds 100 Gbps)
- Intel 82599 Virtual Function (VF) (Network speeds 10Gbps - legacy option)

Used for High throughput applications which require higher bandwidth.

#### EFA - Elastic Fabric Adapter
Network device that you attach to your n/w to acclerate HPC(High performance Computing) and machine learning application.
EFA can use OS-bypass and gives very low latency, but not supported Windows only Linux.

Answer to you are doing HPC or ML what network adapter you should use?
Ans- Elastic Fabric Adapter


## EC2 Hibernate
- EC2 instance hibernate will save the in memory RAM to EBS root volume. RAM contents are reloaded, the process that were previously running on the instance are resumed, so bootup is quite fast.
- Instance RA cannot be more than 150 GB.
- Instance famlies include c3,c4,c5,m3,4,5,r3,4,5, t3 etc
- Instances cannot be hibernated for more than 60 days.
- Availaible for On demand instances and reserved instances.


## AWS HPC - Hi performance compute
use cases like - genomics, finance risk modeling, weather prediction and even autonomous driving.

Data transfer to AWS -  
1. snowball and snow mobile
2. aws data sync (s3,efs, or FSX for windows) - agent on a virtual machine in our on premise data center
3. direct connect (dedicated n/w between a data center to AWS (not going through internet))

Compute and Networking -
1. Ec2 instances that are GPU or CPU optimized
2. Ec2 fleets(Spot instances or spot fleets)
3. Placement groups (cluster)
4. Enahanced networking - ENA (Elastic Network adpaters  (SR- IOV))
5. Elastic fabric Adapter(EFA) - has OS bypass, higher throughput than traditional TCP in cloud based system
6. Instance attached storage - EBS and Instance store(millions of IOPS; low latency)
Networking storage - 
7. S3 (Distributed object storage not file system)
8. Amazon EFS (can use provisioned IOPS)
9. Amazon FSx for Lustre for HPC

Orchestration and automation -
10. AWS batch - multi node parallel jobs, allows u to run single job that spans multiple ec2 instances
11. AWS parrallel cluster -simple text file model and provision all resources that are needed. Automatic provision of Vpc, subnets, cluster types and instance types
12.



# Questions

- Q: A call center application consists of a three-tier application using Auto Scaling groups to automatically scale resources as needed. Users report that every morning at 9:00 AM the system becomes very slow for about 15 minutes. A Solution Architect determines that a large percentage of the call center staff starts work at 9:00AM, so Auto Scaling does not have enough time to scale out to meet demand.How can the Architect fix the problem?
- A: Create an Auto Scaling scheduled action to scale out the necessary resources at 8:30 AM every morning.

- Q: An e-commerce application is hosted in AWS. The last time a new product was launched, the application experienced a performance issue due to an enormous spike in traffic. Management decided that capacity must be doubled the week after the product is launched.
Which is the MOST efficient way for management to ensure that capacity requirements are met? 
- A: Add a Scheduled Scaling action.

---
- Q: An interactive, dynamic website runs on Amazon EC2 instances in a single subnet behind an ELB Classic Load Balancer.
Which design changes will make the site more highly available?
- A: Move some amazon ec2 instances to a different subnet. 
other option - Change the ELB to an Application Load Balancer- will not work as the AZ goes down , so does your application
----
- Q: A company hosts a popular web application. The web application connects to a database running in a private VPC subnet. The web servers must be accessible only to customers on an SSL connection. The RDS MySQL database server must be accessible only from the web servers.
How should the Architect design a solution to meet the requirements without impacting running applications?
Option1 . Open an HTTPS port on the security group for web servers and set the source to 0.0.0.0/0. Open the MySQL port on the database security group and attach it to the MySQL instance. Set the source to Web Server Security Group.
Option 2. Create a network ACL on the web server's subnet, and allow HTTPS inbound, and specify the source as 0.0.0.0/0. Create a network ACL on a database subnet, allow MySQL port inbound for web servers, and deny all outbound traffic.
- A:  Security groups are at instance level whereas NACL are at subnet level. Editing any NACL can impact other applications at the subnet level.
Hence answer is Open an HTTPS port on the security group for web servers and set the source to 0.0.0.0/0. Open the MySQL port on the database security group and attach it to the MySQL instance. Set the source to Web Server Security Group.


