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

FIGHT-DR-MC-PXZ-AU (Fight DR Mc Pxz Australia)
F FPGA
I IOps
G Graphics
H High Disk Throughput
T t2 Micro - Cheap General purpose
D Density
R RAM
M Main choice for general purpose apps
C Compute
P Graphics (Pics)
X Extreme memory
Z Extreme Memory and CPU
A ARM based workloads
U Bare metal


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
