# IP

TCP/IP

Internet Protocol

v4 - 8 bit octs - so their range is 0 - 2^8(255)
v6 - 128 bits


## IP Address

IPv4 address contains octets(8 bits) , that is their range is from 0 - 2^8(255).

42 in Binary- 00101010

There are 4 octets in an IPv4 address-

127.0.0.1 - reserved by IANA to identify the computer you are using.(Localhost)

IPv4 parts -

Class	Theoretical Address Range	Binary Start	Used for-

| Class         | Theoretical Address Range     |   Size of the network bit field  | Used For             |
| ------------- |:----------------------------- |:---------------------------------|:--------------------:|
|   A           | 0.0.0.0 to 127.255.255.255    |  0              | Very Large Networks  |
|   B           |128.0.0.0 to 191.255.255.255  |	10	             | Medium networks      | 
|   C           |192.0.0.0 to 223.255.255.255	  | 110             | Small networks       |
|   D           |224.0.0.0 to 239.255.255.255   | 1110            | Multicast            |
|   E           |240.0.0.0 to 247.255.255.255   | 1111            | Experimental         |



|Class|Leading bits |	Size of network |number bit field |	Size of rest bit field |	Number of networks | Addresses per network |	Total addresses in class |	Start address	|End address|
|-------|: --------- |:---------- |:--------------- |: ----------------- |:-------------|:----------------|: ------------|: -------------------	|: --------------- :|


### Class A - The first bit of the first octet is always set to 0 (zero).
Binary start = 0
Remaining bits in 1 st octet = 7
That is range = 2^7 = 128 
So First IP octet could range from 0-127 in class A.


### Class B
Binary starts = 10
remaining bits in the first octet = 6
so remaining values allowed = 2^6 = 64
So First IP octet could range from 128 - 191 in class B. (128+64 = 192)

### Class C
Binary Start 110
Remaining bits - 5
So remaining values allowed = 2^5 = 32
So First IP octet could range from 192 -223 in class B. (192+32 = 224)

### Class D
Binary Start 1110
remaining bits - 4
So remaining values allowed = 2^4 = 16
So First IP octet could range from 224 -239 in class B. (224+16 = 240)

### Class E
Binary Start 1111
remaining bits - 3
So remaining values allowed = 2^3 = 8
So First IP octet could range from 240 -247 in class B. (240+16 = 248)


Class C networks use a default subnet mask of 255.255.255.0 and have 192-223 as their first octet. 
Address 192.168.123.132 is a class C address. Its first octet is 192, which is between 192 and 223, inclusive.

## Subnets and Subnet masking

192.168.123.132 is (in binary notation) the 32 bit number
11000000.10101000.01111011.10000100 in binary


  192.168.123. Network .132 Host
  
  192.168.123.0 - network address. 0.0.0.132 - host address.
  
  
 ## Subnet Mask -
  The subnet mask is used by the TCP/IP protocol to determine whether a host is on the local subnet or on a remote network.
example,
If the subnet mask is 255.255.255.0. 
That is in Binary - 11111111.11111111.11111111.00000000 

# The first 24 bits (the number of ones in the subnet mask) are used to identify as the network address, 
with the last 8 bits identifying the host address(the number of remaining zeros in the subnet mask)

So the maximum number of Ip's a Host address with 8 bits can represent is 2^8 = 256. 
Basically all Permutations and Combinations of 00000000.

In this example, Network Id  - 192.168.123.0
Host address - 0.0.0.132. 

When a packet arrives on the 192.168.123.0 subnet (from the local subnet or a remote network), 
and it has a destination address of 192.168.123.132, your computer will receive it from the network and process it.


Class A networks use a default subnet mask of 255.0.0.0 and have 0-127 as their first octet.
example, 10.52.36.11 is a class A address. Its first octet is 10


Class A can represent 16777216 IPs in the subnet = you have Subnet mask of 24 bits. 2^24 = 16,777,216
10.x.x.x so 16777216 IPs starting from 10.


Class B networks use a default subnet mask of 255.255.0.0 and have 128-191 as their first octet. 
address 172.16.52.63 is a class B address. Its first octet is 172, which is between 128 and 191, inclusive.




## CIDR notation
P addresses contain 4 octets, each consisting of 8 bits giving values between 0 and 255.
The decimal value that comes after the slash is the number of bits consisting of the routing prefix. 

192.168.123.132/16
IP - 192.168.123.132
Routing prefix - 16

Routing prefix 16 means that there are 16 bits available in the subnet mask to represent address.
Which mean that we can represent 2^16 address using this subnet mask.

First IP that can be represented - 192.168.0.1 
Last IP that can be represented - 192.168.255.254  

16 bits for prefix means = out of 4 octets of 8 bit each =  first 16 bits are fixed for network address, remaining 16 for subnet mask. 
So you start at the range from 0.1 and go to max 255.254.




------------------------------------------------------------------------
© 2019 GitHub, Inc.
Terms
