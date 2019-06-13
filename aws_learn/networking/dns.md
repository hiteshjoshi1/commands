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
```
DNS Resolver --> Query to Root Zone registry in WHOIS Server --> Get the TLD (.com,.gov) and will give the Authoritative NS Record [returns IP or location of an authoritative name server or an error] --> Query Name Server(NS) --> Get SOA (Start Of Authority Record) -->
Start Record has A Record, AAAA record, CNAME, TTL etc.
```
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


### Whois Server -
WhoIs Server at whois.iana.org is used for looking information on several regosteries maintained as a part of IANA functions -
1. __Root Zone Registry__ — the WHOIS database of delegations from the DNS root zone (also know as top-level domains).
This is replicated in the 13 root clusters.
2. .INT Registry — the database of .INT domain registrations, used by intergovernmental treaty organisations.
3. .ARPA Registry — the database of .ARPA domain registrations
4. IPv4 and IPv6 allocations — the registry of allocations made from the global IPv4 and IPv6 address spaces, plus specially designated allocations described in technical standards.
5. Autonomous System (AS) number allocations — the registry of allocations made from the global AS number space.


Unique list of domain names maintained by ICANN. A regitrar (example aws or GoDaddy) will use the InterNIC service of ICANN to register a Domain.




__DNS Zone__ -
The domain name space of the Internet is organized into a hierarchical layout of subdomains below the DNS root domain.
The domain name space is partitioned into  these areas (zones) so that they can be managed independently.A DNS zone is a distinct part of the domain namespace which is delegated to a legal entity—a person, organization or company, who are responsible for maintaining the DNS zone. 

A DNS zone is implemented in the configuration system of a domain name server. Historically, it is defined in the zone file, an operating system text file that starts with the special DNS record type Start of Authority (SOA) and contains all records for the resources described within the zone. 

Most top-level domain name registry operators offer their name spaces to the public for registration of second-level domains. Similarly an organization in charge of a lower level domain may operate its name space similarly and subdivide its space.

DNS Zone file (on DNS Server) has following components -

__CNAME Record__ -

CNAME or Canonical Name links an alias name to another true or canonical domain name.
for example - www.example.com m and mobile.example.com


__A Record__-
IPv4 Address Mapping records (A)—a hostname and its IPv4 address.
Mapping of the IP address to Host Name.

__AAAA Record__ -
IPv6 Address records (AAAA)—a hostname and its IPv6 address.

__NS Record__
Name server (NS) records determine which servers will communicate DNS information for a domain. Generally, you have primary and secondary name server records for your domain. 

__SOA Record__
Start of Authority
This is one larger record at the beginning of every zone file with the primary name server for the zone and some other information. 
A DNS Server that manages a specific domain is called the Start of Authority(SOA) for that Domain.
The SOA record specifies core information about a DNS zone, including the primary name server(NS), the email of the domain administrator, the domain serial number, and several timers relating to refreshing the zone.

DNS servers cache results until the TTL.

ISP DNS -->Root Name Server --> SOA(example amazon SOA or google SOA) -->IP

__Mail Exchanger(MX)__

Mail Exchange (MX) records direct a domain's email to the servers hosting the domain's user accounts.  
The MX records allows you to point your mail services somewhere other than your hosting company (example GoDaddy) if you choose to use something like Google Apps for your domain. For example, people who use Google for the e-mail for their domain will create an MX record that points to ghs.google.com.

__Reverse-lookup Pointer records (PTR Record)__—
Allows a DNS resolver to provide an IP address and receive a hostname (reverse DNS lookup).

__Certificate record (CERT Record)__ -
Stores encryption certificates—PKIX, SPKI, PGP, and so on.


Root zone
Managed by IANA. Operated by 13 servers from organizations such as Verisign ,NASA.

TLD Zones-
.gov,.com, .co.uk etc - over 1500 TLD domains. Managed by IANA

Domain Zones-
Second-level domains like the domain you are viewing now, “ns1.com”, are defined as separate DNS zones, operated by individuals or organizations. Organizations can run their own DNS name servers, or delegate management to an external provider.
example - ns1.google.com



-------------------------------------------------------------------


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


# ICANN
Internet Corporation for Assigned Names and Numbers
A nonprofit private American corporation that oversees global IP address allocation, autonomous system number allocation, root zone management in the Domain Name System (DNS), media types, and other Internet Protocol-related symbols and Internet numbers.

## IANA
The Internet Assigned Numbers Authority (IANA) is a function of ICANN. IANA is however now under private sector.
IANA administers the data in the root nameservers, which form the top of the hierarchical Domain name system (DNS) tree.

IANA delegates allocations of IP address blocks to regional Internet registries (RIRs). Each RIR allocates addresses for a different area of the world.Collectively the RIRs have created the Number Resource Organization formed as a body to represent their collective interests and ensure that policy statements are coordinated globally.


