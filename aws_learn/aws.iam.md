# Identity and Access management

### Users
You create a user and can give him -
  1. Programmatic access (With access key id and secret key)
  2. AWS Management Console

### Groups
A user can be added to a user group. Groups are governed by policies and policy need to be specified while creating a group.

### Policy
Are JSON files which define access rules.

### Roles 
When an AWS service wants to talk to another AWS Service they need to have the right permissions called Roles.
Example, EC2 Instances can access S3 will require AWSS3FullAccess role.


### Notes-
- User, roles, groups ,policies are global by default.
- Admin user - can do everything including changing the access in IAM
- Power User - can do everything except management of grops and users within IAM.
- By default new User in AWS will have no access

