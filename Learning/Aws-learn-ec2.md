# EC2 - Elastic Compute cloud

Pricing philosophy(Not needed for exam)

- Pay as you go and pay for what you use
- Pay less as you use more
- Pay even less when you reserve capacity

## EC2 Pricing Models -

- On Demand
- Reserved
- Spot - Price moves around
- Dedicated Hosts

### On Demand -
Low cost, no upfront fee and no long term commitment
Good for 1st time amazon AWS users
Good for short term, spiky or unpredicatble workloads that cannot be interrupted

### Reserved Pricing -

Used for predictable usage
Upfront payments lead to cheaper pricing, 1 or 3 years instances

    + Standard Reserved Instances -
    75% cheaper, more you pay upfront, longer the contract, higher the discount.
    You cant convert one reserved instances to other instances.
    
    + Convertible Reserved Instances - 
    You can convert one reserved instances to another.
    
    + Scheduled Reserved Instances -
    Available within the time windows you reserve.
    
### Spot Pricing - Might use this for own websites
AWS selling off its unused inventory.
Applications that have flexible start and end times.
Applications that are only feasible at very low compute prices.

### Dedidicated Host Pricing

Useful for regulatory requirements which do not allow multi tenant virtualization.
Can be purchased ON -Demand or at Reserved Pricing(Discounted 70% of On Demand).


### EC2 Instance Types - {Not required for Soln Arch Assoc exam}

FIGHT-DR-MC-PXZ-AU
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

### EC2 Security -
### Security Group - 
This is the place where you create inbound and outbound rules for access to Ec2 instance( this will be a rule analogus to Inbound/ outbound rules in Azure). 
You will create a Security Group that has inbound and outbound Security Rules. Security groups are created for a VPC(Virtual Private Cloud).

KeyPair - Create public private key pair(or use existing) that will allow you to access your instance.(This will be a .pem file)


- You cannot Block individual IPs using Security Groups. Use NACL for that (Network Access Control List).
- No Block rules are allowed, by default everything is blocked and rules allow specific access.
- All Inbound traffic is blocked by default and we enable rules to allow access.
- All Outbound traffic is allowed. 
- Changes to Rules in Security Group takes place immediately.
- You can add more than one Security Group to an Ec2 Instance.

- Termination protection is disabled by default, enable it for termination protection of EC2 instance.
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

8. Put your static website under  -
/var/www/html/

Apache will serve the website at the public IP of AWS EC2.

    
