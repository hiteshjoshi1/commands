# Command Line

ssh ec2-user@i/p -i <PEM file>

sudo su

To configure User-> This would require the Csv file of user for credentials
aws configure

See all S3 ->
aws s3 ls

Create an Aws bucket - name should be unique
aws s3 mb s3://my_fancy_aws_bucket_name

To see your creds in AWS -
cd ~
Hidden directory
cd .aws
cat credentials


https://docs.aws.amazon.com/cli/latest/reference/
