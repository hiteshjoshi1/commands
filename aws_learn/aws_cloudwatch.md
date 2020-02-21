# Cloudwatch

Used for Performance Monitoring 

__Monitor Compute__
- EC2 instances
- Autoscaling groups
- Elastic Load balancers
- Route53 Health checks

__Monitor Storage and CDN__
- EBS Volumes
- Storage Gateways
- Cloudfront

-- Billing Alarms etc.

### Cloudwatch with EC2  -
- CPU 
- Network
- Disk I/O
- whether Underlying Hypervisor is running or not


### Mintoring times
Standard monitoring - 5 mins
Detailed Monitoring - 1 mins

Cloudwatch with EC2 will monitor events every 5 mins by default.Can have 1 min monitoring.
Can set up alarms which wil trigger notifications.
   - Example Billing Alarms
Create Alarms and send emails - example CPU Utilization 
You can also Stop , Restart instances using Cloudwatch Alarms.

We can create Cloudwatch monitor direct through the EC2 instance (Enable Cloudwatch Monitoring) 
or
Go to Management and Governance -> Cloudwatch

You can create Dashboards- based on Region or global dashboards.

**Cloudtrail - Audit Service for AWS - who (which IP address) does what in AWS Management console and API actions.When the calls were made , what was the IP etc.

Cloud Events - Helps you respond to state changes in your AWS resources.
Logs  - helps to aggregate, monitor and store logs. 


