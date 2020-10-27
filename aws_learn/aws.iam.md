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

#### Cloud Directory

Directory based store for developers, can store hierarchies with hundreds of millions of developers.
can be used to Org charts, course catalogues, or device registries.
- Non AD compatible

#### AWS Cognito user pools

- managed user directory for SaaS applications.
- Sign up or sign in for web or mobile applications
- Works with Social media identites(federated identity)
- non AD compatible












