# Elastic Load Balancers

Balance load balancer 

1. Application Load Balancers
2. Network Load Balancer
3. Classic Load Balancer

## Application Load Balancers -
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


A classic LB is sort of a dumb router which will route traffic to your EC2 instances randomly.

### Application load balancers
1. create target groups - can be done based on Instance(ec2), IP, or Lambda function.
2. Use the target group when creating the application Load balancer, you can define advance routing in application Load Balancer .

#TODO - Read the FAQ of Load Balancer, not done thoroughly


### Sticky Sessions
Classic load balancers route the traffic to EC2 instances with the smallest load.
Sticky sesisons allows you to bind a user session to a specific EC2 instance on a classic load balancers. This ensures all the request from the user during a session are served by the same instance.

You can enable sticky session on an Application Load Balancer as well, but the traffic would be sent at target group level.


### Cross Zone load Balancing
Across zone load balancing can be done using Load balancers in different Availability zones.

### Path Patterns

Path based Routing - routing is done based on the URL path.






