# Elastic Load Balancers

Balance load balancer 

1. Application Load Balancers
2. Network Load Balancer
3. Classic Load Balancer

## Application LB -
1. Load balancing of http and https traffic
2. Operate at layer 7 and are application aware.
3. Can do advace request routing - sending specified request to specified web servers etc

## Network Load Balancers

1. Best suited for tcp traffic where extreme performance is required.
2. Operates at connection level, Layer -4.

## Classic Load Balancers
1. Legacy LB
2. Can use Layer 7 features - X-forwared and sticky sessions.
3. Can use strict level 4 balancing that rely on purely tcp protocol.
4. cheaper.

Elastic LB  will return 504 error, which means GATEWAY Timeout, that is either application or database went down.

Elastic load balancers will have their own IP(example 10.0.0.23), if you want to get end user IP address for a request coming through ELB,
you can use X-Forwarded-For.

