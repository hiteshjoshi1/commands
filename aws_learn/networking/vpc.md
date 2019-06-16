# VPC - Virtual Private cloud
  - So far we have been using default VPC. All subnets in default VPC have internet access. Each Ec2 instance has both public and private IP address.
  

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

Create Subnets - 1 public subnet and 1 private. Subnets are both private , that is they do not have public IP assigned. Change subnet settings to allow public Ips.

Subnet > Modify > Modify Auto assign IP settings

4. Create Internet Gateway -

Allows communication between instances in the VPC and the internet. It does 2 things -
1.Provide a target in your VPC route tables for internet-routable traffic.
2.To perform network address translation (NAT) for instances that have been assigned public IPv4 addresses.




To enable internet access to or from the internet for instances in a VPC subnet, you must do the following:

- Attach an internet gateway to your VPC.(Create one--> detached --> attach to a VPC).

- Ensure that your subnet's route table points to the internet gateway.

- Ensure that instances in your subnet have a globally unique IP address (public IPv4 address, Elastic IP address, or IPv6 address).
- Ensure that your network access control and security group rules allow the relevant traffic to flow to and from your instance.

5. Route tables -

There is a default route table that is created with the VPC and it allows communication between the subnets.

We want only a specific subnet to be able to communicate with the Internet so we will create a new Route table.

Create a route to allow 0.0.0.0/0

Edit subnet association in the route table and attach the public subnet in the route table.



Note- Security Groups cannot span VPC's.


## NAT - Network Address Translation
Allows Ec2 instances in private subnets have access to internet to may be install software.

Nat Instances(ec2 -  instance , older)  and NAT Gateways(Highly availaible gateway - used now).

NAT Instance -

Create using Amazon community instances -> search NAT and hit enter.

Create the NAT in your VPC in the same AZ where the public Subnet is.

Edit the route table of the VPC, add a route to the __instance__ of NAT. This will give the subnet access to subnet.





