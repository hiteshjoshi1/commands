# AWS EMR (Elastic Map Reduce)
is used for big data processing using tools such as Apache Spark, Apache Hive, Apache Hbase, Apache Flink, Apache Hudi and Presto.

Cluster -> collection of ec2 instances. Each instance in a cluster is called a node. 
Node types -
1. Master Node
2. Core Node
3. Task Node

- Master Node - tracks the status of tasks and monitors the health of the cluster. Every cluster has to have a master node.
- Core Node - A node with software components that runs tasks and stores data in Hadoop Distributed File System(HDFS). Multi node clusters have atleast 1 core node.
- Task Node - A node withs software cmponents that only runs tasks and does not store HDFS. Tasks nodes are optional.

All log data is stored in master nodes /mnt/var/log.

So in order to persist you can archive the log files to S3 every 5 mins. This archiving job(moving log data to S3) has to be done while creating the cluster.
