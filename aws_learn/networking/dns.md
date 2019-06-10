# How does internet work - ELI5

Interact with internet - you need a website address.

example- http://www.google.com/test.html

This website address in Comp Sci Lingo is called a URL - Uniform Resource Locator.
The URL or website address is meaningless to computers, in the internet address of computers is based on IP (example 103.6.149.81).

How is a URL gets translated to an IP - 

URL  has three parts -
1. Protocol Specifier - http
 www - world wide web.* 
2. Domain Name - google
3. com - top level domain (TLD)
4. Page location - test.html

The protocol specifies which port would be used at the server. 
http - 80
ftp - 20,21
smtp - 25
 
The User's OS creates a TCP connection -- then make the HTTP request. In order to create a TCP connection, the IP of Google.com is needed.

Main Process -
Browser --> Operating System --> DNS Resolver(ISP or Google.com or OpenDNS)-->IP

Detailed Process -
DNS Resolver --> Query to Root DNS Server -->A-NS [returns IP or location of an authoritative name server or an error]
Root Server --> returns a list of 13 locations of Authoritative gTLD(or ccTLD servers) Name  servers
DNS Resolver --> iterative query to gTLDs NS -- the TLDs return the Name Servers (NS) of the domain  --> TLD will return a list of all name servers of the domain.

Example google.com has 4 Name servers -
ns1.google.com
ns2.google.com
ns3.google.com
ns4.google.com

Finally the DNSResolver queries one the name Servers for the IP of google.com

At the point the user's operating system has the IP of the server and it can start a TCP handshake.

TLD types
1. ccTLD - country codes, run by government organizations
2. gTLD - Generic TLDs, run by different commercial entity responsible for running these servers, example Verisign.


Root Servers - 
13 root server clusters [named A-M] with servers in 380 locationsin the world. The root servers are managed by 12 different organizations that report to IANA (Internet Assigned Numbers Authority)
All servers are copies of a master server run by IANA.

Root Servers hold the locations of all Top Level Domains(TLDs) example .com, .gov.


### Root Zone database -
Database maintained by IANA of all the Top Level Domains. This is replicated in the 13 root clusters.

### Whois Database -
Unique list of domain names maintained by ICANN. A regitrar (example aws or GoDaddy) will use the InterNIC service of ICANN to register a Domain.


## SOA Records
A DNS Server that manages a specific domain is called the Start of Authority(SOA) for that Domain.

DNS servers cache results until the TTL.

ISP DNS -->Root Name Server --> SOA(example amazon SOA or google SOA) -->IP


Zone file (on DNS Server) components -

__CNAME Record __ -

CNAME or Canonical Name links an alias name to another true or canonical domain name.
for example - www.example.com may be linked to the naked domain example.com

__A Record__-
Mapping of the IP address to Host Name.

__NS Record__
Name server (NS) records determine which servers will communicate DNS information for a domain. Generally, you have primary and secondary name server records for your domain. 

__SOA Record__
Start of Authority
This is one larger record at the beginning of every zone file with the primary name server for the zone and some other information. 

__Mail Exchanger(MX)__

Mail Exchange (MX) records direct a domain's email to the servers hosting the domain's user accounts.  For example, people who use Google for the e-mail for their domain will create an MX record that points to ghs.google.com.


-------------------------------------------------------------------

IP Address

IPv4 address contains octets(8 bits) , that is their range is from 0 - 2^8(255).

42 = 00101010

There are 4 octets in an IPv4 address-

127.0.0.1 - reserved by IANA to identify the computer you are using.(Localhost)

IPv4 parts -




------------------------------------------------------------------------

## MAC Address-
Every network interface, both wired and wireless, has a unique MAC address embedded in it by the manufacturer.

Web servers and other computers that need a consistent point of contact use static IP addresses.To make sure that interface always gets the same IP address, IP associates the address with the Media Access Control (MAC) address for that network interface.


## DHCP Server
- How we get IP in our computers and Phones when we connect to WIFI or LAN -

The Dynamic Host Configuration Protocol (DHCP) is a network management protocol used on UDP/IP networks whereby a DHCP server dynamically assigns an IP address and other network configuration parameters to each device on a network so they can communicate with other IP networks.
DHCP can be implemented on networks ranging in size from home networks to large campus networks and regional Internet service provider networks.
A router or a residential gateway can be enabled to act as a DHCP server. Most residential network routers receive a globally unique IP address within the ISP network. Within a local network, a DHCP server assigns a local IP address to each device connected to the network.


----------------------------------

Primary Domain Name - google.com

Sub domain/s- 
www.google.com
mail.google.com
docs.google.com


Domain Registrar -

Companies which sell availaible domain names. Eg GoDaddy
Most of these companies also provide domain hosting.

