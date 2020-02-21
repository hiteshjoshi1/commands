# Command Line

You need to set the user in management console etc before doing this -

ssh user_name@public_dns_name -i <PEM File Name>

Where user names are different based on the OS provisioned
- for Amazon Linux -> ec2-user
- for Ubuntu -> ubuntu
and so on...

```
ssh ec2-user@i/p -i <PEM file>
```

sudo su

To configure User for first time->
This would require the programmatic credential of the user
```
aws configure
```

Once config is done,

**See all S3 ->

```
aws s3 ls
```

**Create an Aws bucket - name should be unique
mb- make bucket

```
aws s3 mb s3://my_fancy_aws_bucket_name
```

### To see your creds in AWS - There is a Hidden directory at the root -
Go to root

```
cd ~

cd .aws

cat credentials
```

The credentials are stored in .aws/credentials file when we do aws configure.

https://docs.aws.amazon.com/cli/latest/reference/

## IAM Roles -

Roles are far more secure than storing your access key Id and private key in individual EC2 instances.

**Create a Role, assign that role to Ec2 instance.
Now you can login without aws configure. If your user has the role above created. So no need to store credentials(access key Id and Secret access key) in hidden files in individual ec-2 instances.

Roles can be assigned to an ec2 instances after they are created. The roles are always global.


Ec2 Instance --> Instance Settings --> Attach Replace IAM role

then add the Role



-------------------
## EC2 Instance metadata

### Get the ec2 - metadata
```
curl http://169.254.169.254/latest/meta-data/
```

### Get user meta data -  get the bootstrap scripts

```
curl http://169.254.169.254/latest/user-data/
```
