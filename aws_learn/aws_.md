# Amazon Redshift
- Used for OLAP
- fully managed
- dataware housing solution

Can be configured as-
Single Node (160 GB)
Multi Node 
	- A multi node has a **Leader Node** which manages client connections and receives queries. It has also has set of **Compute Node** which store data and perform queries (upto 128 Compute Nodes).

Redshift uses advanced Compression based on Columns. Redshift samples your data and automatically selects the most appropriate compression scheme.

__Backups__
- Enabled by default - 1 day
- max backup - 35 days
- Maintains 3 copies of your data - Original, Replica on the compute nodes and a backup in Amazon S3.
- Can asynchronously backup your SNAPSHOTS  into another region for Disaster recovery.
- No charge for leader node hours, only compute node hours
- Charged for backups and data transfer within a VPC

Security -
- Data is encrypted at transit using SSL
- Encrypted at Rest using AES-256
- By default redshift takes care of key management- can use HSM

## Can be only available in 1 AZ.
- Can restore snapshots to a new AZ in case of outage.
