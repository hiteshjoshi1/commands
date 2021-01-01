# Autoscaling groups


1. Groups
   Web Server Grp, Database group etc 
2. Configuration Templates
   Used by groups as a launch template for its Ec2 instances. 
3. Scaling Options
    - Maintaine current instance levels at all times
    - Scale manually
    - Scale based on schedule
    - Scale on demand
    - Use Predictive scaling

- Create a Launch Configuration with an EC2.
- Using the Launch config create an Autoscaling group. Specify the minimum that has to be run and the maximum instances that could be 
provisioned in the event of high load.
- You can use CPU utilization to trigger auto scaling.
