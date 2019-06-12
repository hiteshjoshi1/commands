# Route53

DNS is on port 53. Hence the name Route53.

DNS - Domain Name Service
Human friendly names to IPv4 and IPv6.


IPv4 is a 32 bit field  = 2^32 number of addresses available

IPv6 is 138 bit field = 2^128  number of addresses

.com, .edu,.gov - first level domain name

.com.uk - .uk is top level domain name, .com is second level domain name.

## Top level Domains are controlled - IANA(Internet Assigned Numbers Authority) 

##Domain Registrars
A registrar is an authority that can assign domain names directly under one or more domains. Uniqueness of domains across the interbet is enforced by ICANN using its service InterNIC
Domain registrars use InterNIC to register domain names with ICANN. The domain name is registered when it becomes part of WhoIS database.

Popular domain registrars -
Amazon
godaddy
123-reg.co.uk

--------------------------------------------------


## NS Records
Name Server Records 
Used by Top level Domain Servers to direct traffic to the content DNS Servers which contains the authoritative DNS records.

hiteshjoshi.com ---> top level domain - will give a Name Server Record --> 172800 IN ns.awsdns.com --> query the ns records --> that will give us the start of authority

We get the A record --> Address(IP address)

A Record -
TTL - Time to live- Length that a DNS record is cached on either the Resolving server or the user's own PC. The lower time to live, faster changes to DNS records take propogate throughput the internet.
** Roughly TTL is 48 Hours**

### C Name - Canonical Name
Can be used to map one domain name to the other
For example www.dbs.com can be canonically mapped so that it resoves to mobile.dbs.com for Mobile browsers.

### Alias Records -

Used to map resource record sets in your hosted zone to Elastic Load balancers, Cloud front distributions, or S3 buckets that are configured as websites.

A CNAME cannot be used for a naked domain name(Zone apex record).

# Exam Tips-
- Elastic Load Balancers ELBs do not have a pre defined IPv4 address, you always resolve to them using a DNS name.
- In AWS , given a choice between Alias Record and CName , always use Alias Record.
- SOA records, NS Record, A Record, CNames,MX Records, PTR Records

------------------------
Provisioned -> hiteshjoshi.net
 
Create a Record Set in the Hosted Zone. Every Record Set is created with a Routing policy.

__Routing Policies__ -
1. Simple Routing
2. Weighted Routing
3. Latency based routing
4. Failover Routing
5. Geolocation routing
6. Geoproximity Routing
7. Multivalue Answer Routing

Use Case -
Your App is deployed in 3 Regions, for example

US Virginia
APAC Singapore
Ireland

Routing will allow you to direct traffic across respective servers. This is defined in Route52 routing policies.


### Simple Routing
One record with multiple IP addresses linked to it is Simple Ruting.
In Simple Routing Route53 would return any of the IP values to the end user randomly.

NS Records for AWS -
ns-1780.awsdns-30.co.uk. 
ns-480.awsdns-60.com. 
ns-1380.awsdns-44.org. 
ns-983.awsdns-58.net.
















