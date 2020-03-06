# Kafka

consists of
- Records 
- Topics
- Consumers
- Producers
- Brokers 
- Logs
- Partitions
- Clusters

### Records
 Records can have key (optional), value and timestamp. Kafka Records are immutable. 
 
### Topics
A Kafka Topic is a stream of records ("/orders", "/user-signups").A topic has a Log which is the topic’s storage on disk. A Topic Log is broken up into partitions and segments. Kafka producers write to Topics. Kafka consumers read from Topics.

### Producer
The Kafka Producer API is used to produce streams of data records. 

### Consumer
The Kafka Consumer API is used to consume a stream of records from Kafka.

### Brokers

A Kafka broker runs in a kafka cluster and form a cluster. The Kafka Cluster consists of many Kafka Brokers on many servers.

### Paritions
A topic log consists of many partitions that are spread over multiple files which can be spread on multiple Kafka cluster nodes. Consumers read from Kafka topics at their cadence and can pick where they are (offset) in the topic log. Each consumer group tracks offset from where they left off reading. Kafka distributes topic log partitions on different nodes in a cluster for high performance with horizontal scalability.Topic log partitions are Kafka way to shard reads and writes to the topic log. Also, partitions are needed to have multiple consumers in a consumer group work at the same time. Kafka replicates partitions to many nodes to provide failover.


## ZooKeeper
Kafka uses ZooKeeper to manage the cluster. Zookeeper sends changes of the topology to Kafka, so each node in the cluster knows when a new broker joined, a Broker died, a topic was removed or a topic was added, etc. Zookeeper provides an in-sync view of Kafka Cluster configuration.
#### Electing a controller - 
The controller is one of the brokers and is responsible for maintaining the leader/follower relationship for all the partitions. When a node shuts down, it is the controller that tells other replicas to become partition leaders to replace the partition leaders on the node that is going away. Zookeeper is used to elect a controller, make sure there is only one and elect a new one it if it crashes.

#### Cluster membership -
which brokers are alive and part of the cluster? this is also managed through ZooKeeper.

#### Topic configuration - 
which topics exist, how many partitions each has, where are the replicas, who is the preferred leader, what configuration overrides are set for each topic

#### Quotas -
how much data is each client allowed to read and write

#### ACLs - 
who is allowed to read and write to which topic (old high level consumer) - Which consumer groups exist, who are their members and what is the latest offset each group got from each partition.



 Kafka, Storm, HBase, SolrCloud

