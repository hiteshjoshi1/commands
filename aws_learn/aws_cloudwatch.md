# Cloudwatch

Performance Monitoring of -

__Monitor Compute__
EC2 instances
Autoscaling groups
Elastic Load balancers
Route53 Health checks

__Monitor Storage__
EBS Volumes
Storage Gateways
Cloudfront

**Cloudtrail - CCTV, AWS API Calls - who (IP) does what(in AWS)-- Audit of what was done.

Cloudwatch with EC2 can be used with -
CPU 
Network
Disk
Status Check - Underlying Hypervisor

Cloudwatch with EC2 will monitor events every 5 mins by default.
Can have 1 min monitoring
Can set up alarms which wil trigger notifications.
   - Example Billing Alarms
Create Alarms and send emails - example CPU Utilization 
You can also Stop , Restart instances using Cloudwatch Alarms.

We can create Cloudwatch monitor direct through the instance or  GO to Management and Governance -> Cloudwatch


