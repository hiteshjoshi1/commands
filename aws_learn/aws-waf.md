# AWS WAF - Web Application Firewall

AWS WAF is used monitor to http and https request to:
- Cloudfront, 
- Application load balancer 
- API gateway

It is a Application Layer firewall, or Layer 7 firewall. It can see query string parameter. A physical firewall works on network layer or layer 4.


WAF allows -
1. Allow all request except that ones you specifiy.
2. Block all request the ones you specify.
3. Count request that match properties you specify


Protects against web attacks based on characterstics of web requests -
1. Ip address range
2. Country from which request have originated
3. Values in request headers
4. String that appears in request, regex matching
5. length of requests
6. can check for sql injections and Cross site scripting (CSRF attack)



