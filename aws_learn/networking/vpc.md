# VPC - Virtual Private cloud

Create a VPC -
You need to define IPv4 CIDR address block - example 10.0.0.0/16

By default VPC creation(does not create any subnets), creates
1. Route table
2. Network ACL
3. Security group

Does not create by default -
1.Subnets
2.Internet gateway
--------------------------------------------

### How to create a VPC steps
1. create VPC (10.0.0.0/16)

2. create subnet (specifiy VPC and subnet address range example (10.0.1.0/24 , 10.0.2.0/24)   and availability zone)
   Note -- A subnet cannot span multiple AZ.
3.  Then if needed make one of the subnet public.
Select Subnet --> Modify Auto assign IP  --> Enable auto assign Public IP v4
10.0.1.0/24  -- Public subnet
10.0.2.0/24 - Private subnet

4. Add internet gateway for VPC
Create Internet gateway -- it creates in Detached mode.
Attach to VPC  and can attach it to  newly created VPC.

You can have 1 internet gateway per VPC.

5. Configure Route tables

Note - Ensure that the main route table(default) is private and not exposed to internet.

So create a MyPublicRouteTable in your VPC.

6. Create Route out  in Route table - Edit Routes
Add Routes

Destination 0.0.0.0/0
Target - The Internet Gateway

IPV6 ->  ::/0 
Destination - Internet gateway

7. Edit Subnet Association and add public subnet 
in  the public route table

8.Launch EC2 -- Network VPC
Subnet - public subnet
 
 Launch Ec2 - Network VPC 
 Subnet - private subnet
 
 Security group do not span Sec Group, so while create EC2 . add a new Sec group in new VPC.
 
 9. Now we have 2 Ec2 , 1 in public subnet and 1 in pvt subnet,  and they are in 2 seprate sec group.
 
 10. Create a new Sec group -- why?
 
10.1. Create a new sec group in the new VPC - MyDbSecGroup
10.2. Add Rules - Inbound rules
  ICMP(ipV4)-- 10.0.1.0/24
  HTTP -- 10.0.1.0/24
  https --10.0.1.0/24
  ssh - 10.0.1.0/24
  mysql/aurora - 10.0.1.0/24
  
11. Create NAT Instances(Single) / NAT Gateway(Highly available)

#### Nat Instances - 
Launch EC2 in PUBLIC subnet and my VPC - use community AMI's and search for NAT instances, WebDMZ
**Disable Source and Destination checks in NAT instances in NAT's Ec2 machine.

There must be a route out from pvt instance to the NAT instance for this to work. for this -->
Edit routing table(main) of your VPC, add a route to internet (0.0.0./0) to NAT insatnces.

#### NAT gateway (preferred way as it is highly available)
Create a NAt gateway in our new subnet which is public.
--Create a new Elastic IP Address.

Then edit main route table of your VPC, add a route to internet (0.0.0./0) to NAT Gateway.


 
#### Network ACL(Access Control Lists) -- Optional as default exists
Default created with VPC, Allow And deny rules.

Can create your own New NACL in your VPC -- by default everything is denied in rules.
Associate with public subnet

Then add rules in NACL , inbound rules for 80(http), 443(https) and 22(ssh)  and epheremal ports -> 1024-65535
Outbound rules (http, https and epheremal ports -> 1024-65535 )

Epheremal ports are required for s/w update and all.

NACl rules ... are evaluated top down from Rule#. So Allow All rule on top will override any deny rules down below.

A NACL can be associated with multiple subnets.
NACL run before Security groups settings.
Each subnet is asscoaited with a NACL, if not specified it is associated with default NACL.

NACL - rules need to be added  seprately for inbound and outbound.

-----------------------------------------


Logically isolate section of AWS where you can control Virtual n/w environment including IP addres, subnets, configuration of route tables, network gateways.
  - So far we have been using default VPC. All subnets in default VPC have internet access. Each Ec2 instance has both public and private IP address.
  
  Can connect to a VPC from outside using
  1. Internet Gateway
  2. Virtual Private gateway.
  
  VPC is typically a collection of -
  1. Router
  2. Route table
  3. Network ACL
  4. Security Group in public net and Sec Group in pvt subnets
  5. Bastion hosts
  

A VPC allows you to create a virtualized enviornment where you have complete control over 
- Selecting IP address Range
- Creation of Subnets
- Configuration of route tables
- Network gateways

For example you can configure the following:
- Webserver can be in a public facing subnet.
- Whereas databases and application servers are in a private subnet not exposed to the internet.
- In addition Security groups and Network ACL(Access Control Lists) can be created to control access to EC2 instances in each subnet.
- **1 subnet cannot be in multiple availability zones.**
- However a AZ can have multiple subnets.

- You can also create a Hardware VPN(Virtual private network) connection between a on-prem corporate data center and amazon VPC, so that you can use AWS cloud as an extension of the corporate data center.

```
Region--> VPC --> [Internet gateway and Virtual Private Gateway] ---> Router --> Router Table --> Network ACLs(Stateless)--> Security Groups(Stateful) -->[Public Subnets and Private subnets]
```


**Network ACLS allows you to do allow and deny rules, which means you can block specific IP's.**

## VPC peering

- Allows you to connect one VPC with another with another via direct network route using private IP address.
- You can pair VPCs with other VPC's and with VPC's in other AWS accounts.
- You can peer VPC between regions.
- VPC peering is not transitive. It is a star config, 1 central VPC pairs with 4 others.

### When we create a VPC in AWS, we by default create -
1. Routing table
2. Network ACL
3. Security Group

You have these 3 created when we create a VPC.

4. Create __Subnets__ - 
1 public subnet and 1 private. Subnets are both private by default , that is they do not have public IP assigned. Change subnet settings to allow public Ips.

Subnet > Modify > Modify Auto assign IP settings

5. Create __Internet Gateway__ -

Allows communication between instances in the VPC and the internet. It does 2 things -
1.Provide a target in your VPC route tables for internet-routable traffic.
2.To perform network address translation (NAT) for instances that have been assigned public IPv4 addresses.


To enable internet access to or from the internet for instances in a VPC subnet, you must do the following:

- Attach an internet gateway to your VPC.(Create one--> detached --> attach to a VPC).

- Ensure that your subnet's route table points to the internet gateway.

- Ensure that instances in your subnet have a globally unique IP address (public IPv4 address, Elastic IP address, or IPv6 address).
- Ensure that your network access control and security group rules allow the relevant traffic to flow to and from your instance.

6. __Modify Route tables__ -

There is a default route table that is created with the VPC and it allows communication between the subnets.

We want only a specific subnet to be able to communicate with the Internet so we will create a new Route table.

Edit subnet association in the route table and attach the  public subnet.

Create a route to allow 0.0.0.0/0 through our internet gateway(target)



Note- Security Groups cannot span VPC's.


## NAT - Network Address Translation
Allows Ec2 instances in private subnets have access to internet to may be install software.

Two types 
1. NAT Instances(individual ec2 -  instance , not highly available - Older)  
2. NAT Gateways(Highly availaible gateway - used now).

### NAT Instance -

1.Create using Amazon community instances of EC2 -> search NAT and hit enter.

2. Create the NAT in your VPC in the same AZ where the public Subnet is.

3.Edit the route table of the VPC, add a route to the __instance__ of NAT. This will give the subnet access to subnet.

4.Single point of failure , which is a bottleneck for all machines that dependent on NAT instance for internet access.

5. ** When creating a NAT Instance disable Source and destination check on that instance.

6. NAT instances should be in public subnet.

7. There must be a route out of the public subnet to the private subnet for this to work.

8. They have to be created behind a security group.

9. The traffic a NAT instance can handle depends on its instance size. You can increase the instance size and manually create autoscaling groups, multiple subnets in different AZs and a script to automatic failover.

10. Due to point 9, NAT instances are on their way out.

### NAT Gateway -

1. Create a NAT gateway using your public subnet.

2. Auto assign an IP to it.

3. Add the NAT gatweway to the default routing table of VPC, which will let ALL SUBNETS access to it.
Destination = 0.0.0.0/0 
Target  = NAT ID

4. Can only be one NAT instances in an Availability zones.
5. Are not associated to a Security Zones.
6. No need to disable any source and destination checks - config is straightforward
7. If resources are in multiple AZ share a NAT gateway. If the NAT gateway is down with a AZ, the resources in other AZ will also loose access.
Recommended -  Create one NAT per AZ so that instances in other AZ are not affected if this AZ goes down.


## Network Access Control Lists (NAC) -- Are linked to Subnets-- and Ec2 instances are created in VPC and in a subnet

1. When we create a VPC, a  default network ACL is created.
2. Everytime a subnet is created , it is added to default network ACL.
3. You can create a new ACL and then change subnet association from default ACL to your newly created ACL.
4. A subnet can only be associated to one ACL at a time.  So when you add a subnet to your new ACL , it's association will be removed from the default network ACL.
5. An ACL can however can associate with multiple subnets which it governs.
6. You can have deny rules in ACL, however **Rules are evaluated top down**. So if you have a deny rule , make sure that its rule # is less than a Allow Rule.
7. Network ACL act before Security groups. So if anything is denied at network ACL, it will never reach Security group.
8. By default , in a new network ACL's - it blocks all inbound and outbound traffic.
9. Network ACL are stateless, need to add specific inbound and outbound rules seprately(Unlike Sec groups).


### VPC Flow Logs

1. VPC flow logs is a feature that enables you to capture IP traffic going in and out of your network interface to your VPC.
2. Flow data is stored in AWS Cloudwatch Logs or S3 buckets and can be viewed from there.
3. Can be created at 3 levels -
  - VPC
  - Subnet
  - Network interface level
4. cannot create a flow log for VPC's peered with your VPC unless that VPC is also within your a/c.
5. Cannot tag a flow log
6. After a flow log is created it config cannot be changed, example using a different IAM log with the flow log.
7. Not all IP is monitored -  
    - Traffic generated by instances when they contact amazon DNS server is not monitored. If you use your own DNS server, then it is minitored.
    - DHCP traffic.
    - traffic generated by amazon windows instances for windows license activation.
    - traffic to the reserved IP address of default VPC router.
    - traffic to and from 169.255.169.254 for instance metadata
    
    
## Bastions
Bastion Host - designed and congfigured to withstand attacks, generally has one application like a proxy server,all other services are removed to reduce the threat to this computer. Stays outside firewall or in a DMZ.
You can get Bastion AMIs from Aws marketplace.

A NAT gateway or NAT instance is used to provide internet connectivity to Ec2 instances in private subnets.Bastions are also called Jump boxes. A bastion host can be used to securely administer ec2 instances.

### Direct Connect
Connects your data center to AWS.
Userful high throughput workloads.
Stable or reliable secure connection.


## VPC endpoints 

- VPC end point enables you to privately connect your VPC to supported AWP services and VPC endpoint
services powered by private link without requiring an Internet gateway and Nat device a VPN connection
or an AWP Direct Connect connection. 

- Instances in your VPC do not require public IP addresses to communicate with resources in the service, so traffic between your VPC and other services does not leave the Amazon Network.

You don't need to go over the Internet. 
VPC endpoints are horizontally scaled and highly available.

Types of VPC endpoints- 
1. Interface endpoints
2. Gateway endpoints

Interface endpoints - is an __ENI (Elastic Network Interface)__ with a private IP address that serves as an endpoint for traffic destined for that service.


VPC Gateway endpoints - supported for Dynamo DB and S3 currently.


NOT CLEAR - Bastions and VPC Endpoints

 
