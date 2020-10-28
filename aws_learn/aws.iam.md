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

### ARN - Amazon Resource Name


Any resource can be uniquely identified with an ARN.

arn:partition:service: region:accountId:   resource/resource_type, resource: qualifier
1. partition - aws, aws-cn (AWS china partition)
2. service - s3, ec2, rds, 
3. region - us-east-1 , eu-central-1 
4. 12 digit account id

Examples
1. arn:aws:iam::1234567:user/hitesh (where 1234567 is accountId, user is resource type and hitesh is the resource)
2. arn:aws:s3:::my_bucket_name/image.png (an image in s3)
3. arn:aws:dynamodb:us-east-1:1223455:table/orders (a table in a user account in dyanamo db)
4. arn:aws:ec2:us-east-1:1223445: instance/* (All ec2 instances in a region and an account 1223445)

### IAM Policies

2 types of IAM policies
- Identiity policies ( attached to IAM user, group or role)
- Resource based policies (attached to resources SQS queues, S3 buckets,KMS encryption keys)

A policy has to be attached to have an effect.A policy document is a list of statement in JSON.

Any that is not explicitly allowed == implicitly denied
Explicit deny > everything else 
AWS joins all applicable polciies

Policies can be:
- AWS managed policies 
- Customer managed policies.
- Inline policy

### Permission Boundaries

- Used to delegate administration to other users
- AWS supports permissions boundaries for IAM entitiees(user and roles)
- prevent privelege escalaton or unnecessarily broad permissions.
- control maximum permissions an IAM policy can grant

Use cases for permissions boundaries:
- Devs creating roles for lambda functions.
- Application owners creating roles for ec2 instances.
- admins creating adhoc users.

Say a user with Administrator Access --> apply Permission boundaries --> give say Dynamo Db full access


## Advanced IAM

### AWS Directory Services
1. Managed AD
2. Simple AD
3. AD Connector
#### Managed Micorosft AD
- Family of managed services
- connects AWS resources with on-premise AD.
- use existing corporate credentials
- SSO to any domain joined EC2 instances.

- Active Directory (Ldap and DNS) has to be highly available.
- Uses Kerberos, LDAP and NTLM authentication 
- Provides AD domain controllers(DCS) running windows server
- reachable by application in your VPCs
- Add additional Domain controllers (DCS) for HA and performance.
- Customer has exclusive access to DCs
- Extend existing AD to on premise  using **AD TRUST

**AWS responsibility in managed AD

- AWS will do multi AZ development
- AWS will patch, monitor, recover
- Instance rotation
- Snapshot and restore

**Customer responsibility

- User, groups and Group Policy objects(GPO)
- using Standard AD tools
- Scale out Domain controllers
- Create AD Trusts(resource forest)
- Certificate authorities using LDAPS
- AD Federation

#### Simple AD
- Standalone managed directory
- Windows workloads that need basic AD features
- Small < =500 ; Large <= 5000 users
- Easier to manage Ec2 instances using existing corporate credentials
- Cant join trusts - so cant join on-premise AD.

#### AD Connector

- Directory Gateway (proxy) for an on premise AD
- Avoid caching information in the cloud
- Allows on premise users to log on to AWS using AD.
- Join Ec2 instances using to your existing AD domain
- Scale across multiple AD connectors.
- AD compatible

#### Cloud Directory

Directory based store for developers, can store hierarchies with hundreds of millions of developers.
can be used to Org charts, course catalogues, or device registries.
- Non AD compatible

#### AWS Cognito user pools

- Managed user directory for SaaS applications.
- intended for Sign up or sign in for web or mobile applications
- Works with Social media identites(federated identity)
- non AD compatible












