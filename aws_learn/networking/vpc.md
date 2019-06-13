# VPC 
Virtual Private cloud

A VPC allows you to create a virtualized enviornment where you have complete control over 
- Selecting IP address Range
- Creation of Subnets
- Configuration of route tables
- Network gateways

Example - 
Webserver are in a public facing subnet
Whereas databases and application servers are in a private subnet not exposed to the internet.
In addition Security groups and Network ACL(Access Control Lists) can be created to control access to EC2 instances in each
subnet.

- You can also create a Hardware VPN(Virtual private network) connection between a on-prem corporate data center and amazon VPC, 
so that you can use AWS cloud as an extension of the corporate data center.

```
Region--> VPC --> [Internet gateway and Virtual Private Gateway] ---> Router --> Router Table --> Network ACLs(Stateless)--> Security Groups(Stateful) -->[Public Subnets and Private subnets]
```


Network ACLS allows you to do allow and deny rules, which means you can block specific IP's.

