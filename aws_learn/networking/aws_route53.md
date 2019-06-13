# Route53

DNS is on port 53. Hence the name Route53.

DNS - Domain Name Service
Human friendly names to IPv4 and IPv6.

ELB- Elasic Load Balancers do not have predefined IP v4 address, you resolve to them using a DNS Name.


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

------------------------
NS Records for AWS -
ns-1780.awsdns-30.co.uk. 
ns-480.awsdns-60.com. 
ns-1380.awsdns-44.org. 
ns-983.awsdns-58.net.
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
 


After you register your domain name, Route 53 automatically creates a public hosted zone that has the same name as the domain.

### Records in Route53 
To route traffic to your resources, you create records, also known as resource record sets, in your hosted zone. 

Each record includes information about how you want to route traffic for your domain, such as the following:

__Name__
The name of the record corresponds with the domain name (example.com) or subdomain name (www.example.com, retail.example.com) that you want Route 53 to route traffic for.
The name of every record in a hosted zone must end with the name of the hosted zone. For example, if the name of the hosted zone is example.com, all record names must end in example.com. The Route 53 console does this for you automatically.

__Type__
The record type usually determines the type of resource that you want traffic to be routed to. For example, to route traffic to an email server, you specify MX for Type. To route traffic to a web server that has an IPv4 IP address, you specify A for Type.

__Value__
Value is closely related to Type. If you specify MX for Type, you specify the names of one or more email servers for Value. If you specify A for Type, you specify an IP address in IPv4 format, such as 192.0.2.136

__Routing Policies__ -
1. Simple Routing
2. Weighted Routing
3. Latency based routing
4. Failover Routing
5. Geolocation routing
6. Geoproximity Routing
7. Multivalue Answer Routing

Use Case -
Your App is deployed in 3 Regions, for example -

US Virginia
APAC Singapore
Ireland

Routing will allow you to direct traffic across respective servers. This is defined in Route52 routing policies.


### Simple Routing Policy
One record with multiple IP addresses linked to it is Simple Ruting. - need to create only one Simple Routing policy with multiple IPS in different lines.
In Simple Routing Route53 would return any of the IP values to the end user randomly.

### Weighted Routing policy
Split traffic based on the weights assigned.
Example-
70% traffic goes US Virginia
20% traffic to SG
10% traffic to Ireland.

You can create health checks for individual IP's(A records). If a record fails it would be removed from Route53. You can also set alarms if the healthcheck fails.

### Latency Based Routing Policy
Route the traffic based on least network latency for the end user of the site.

Create 3 policy of type latency based for each IP. Route 52 will redirect the user based on where he is getting the least network latency.

### Failover Routing

Has a primary(Active site) and a secondary(Passive Site). It is mandatory to have a health check on primary for failover routing.
Primary goes down , traffic is routed to Secondary.

### Geo Location Routing 

Based on the Geolocation Routing

Europe origin goes to a European customer. APAC routes can be routed to Singapore.

### Geoproximity Routing
Routing is done based on the geolocation of the end user (as in Geo location routing) and also on the basis of our resources.
You can also choose to route more or less traffic to a given resource by specifying a value called Bias.

Note - To use geoproximity routing you need to use Route53 traffic flow.
Side Note - The traffic flow visual editor lets you create sophisticated routing configurations for your resources using existing routing types such as failover and geolocation. You save the configuration as a traffic policy and then use it to create one or more policy records. Each policy record routes DNS queries for a specified domain or subdomain.

### Multivalue Answer Route
Same as Simple Routing, but it allows you to put healthcheck on each record. Basically same as Failover routing but with multiple Secondaries. 1 fails go to 2. 2 fails go to 3 and so on.


