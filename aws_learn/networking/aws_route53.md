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
State of Authority Record -
Where DNS going to start


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












