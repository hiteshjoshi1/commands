# Command Line

ssh user_name@public_dns_name -i <PEM File Name>

Where user names are different based on the OS provisioned
for Amazon Linux -> ec2-user
for Ubuntu -> ubuntu
and so on...

```
ssh ec2-user@i/p -i <PEM file>
```

sudo su

To configure User-> This would require the Csv file of user for credentials
aws configure

See all S3 ->

```
aws s3 ls
```

Create an Aws bucket - name should be unique

```
aws s3 mb s3://my_fancy_aws_bucket_name
```

To see your creds in AWS -There is a Hidden directory at the root -
Go to root

```
cd ~

cd .aws

cat credentials
```

The credentials are stored in .aws/credentials file when we do aws configure.

https://docs.aws.amazon.com/cli/latest/reference/

IAM Roles -

Roles are far more secure than storing your access key Id and private key in individual EC2 instances.

Create a Role, assign that role to Ec2.
Now you cannot login with aws configure if you have that role.

Get Instance metadata

```
curl http://169.254.169.254/latest/meta-data/
```

Get user meta data - startup scripts

```
curl http://169.254.169.254/latest/user-data/
```

Ec2 Instance --> Instance Settings --> Attach Replace IAM role

then add the Role
