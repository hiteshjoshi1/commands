# Kubernetes Architecture

When you deploy Kubernetes, you get a cluster.

A Kubernetes cluster consists of a set of worker machines, called nodes, that run containerized applications.
Every cluster has at least one worker node.

Kubernetes architecture of a cluster has 2 main components -
1. Kubernetes Master (can be replicated for availability and redundancy) 
2. Non- master Kubernetes nodes


## Kubernetes Master (Control Pane)
When you interact with Kubernetes, such as by using the kubectl command-line interface, you’re communicating with 
your cluster’s Kubernetes master.The “master” refers to a collection of processes managing the cluster state.
Typically all these processes run on a single node in the cluster, and this node is also referred to as the master.
The master can also be replicated for availability and redundancy.

The master has 3 main components -
1. kube-apiserver
2. kube-scheduler
3. kube-controller-manager 
4. cloud-controller-manager
5. etcd

### kube-apiserver 
Exposes the k8s APIs. This is what kubectl calls when you use kubectl in cli.
Kubectl converts the yaml file to JSON and sends the request to kube-apiserver

### etcd
 etcd is a distributed key-value store, and is used as backing store of all cluster data. All pod definition is stored in here.
 
### kube-scheduler
Component that watches for newly created pods with no assigned node, and selects a node for them to run on. This is based on various factors
such as individual and collective resource requirements, hardware/software/policy constraints, affinity and anti-affinity specifications,
data locality, inter-workload interference and deadlines.

### kube-controller-manager
Component that runs CONTROLLER processes. 
___________________________________
These controllers include:
1. Node Controller: Responsible for noticing and responding when nodes go down.
2. Replication Controller: Responsible for maintaining the correct number of pods for every replication controller 
   object in the system.
3. Endpoints Controller: Populates the Endpoints object (that is, joins Services & Pods).
4. Service & Token Controllers: Create default accounts and API access tokens for new namespaces.
5. Route controller

___________________________________

### cloud-controller-manager
cloud-controller-manager runs controllers that interact with the underlying cloud providers.
cloud-controller-manager allows the cloud vendor’s code and the Kubernetes code to evolve independently of each other. 

___________________________________
The following controllers have cloud provider dependencies:

1.Node Controller: For checking the cloud provider to determine if a node has been deleted in the cloud after it stops responding
2.Route Controller: For setting up routes in the underlying cloud infrastructure
3.Service Controller: For creating, updating and deleting cloud provider load balancers
4.Volume Controller: For creating, attaching, and mounting volumes, and interacting with the cloud provider to orchestrate volumes

___________________________________

## Kubernetes Worker nodes
Has 3 main parts -
1. Kubelet 
2. kube-proxy - a network proxy which reflect K8s networking service on each node.
3. Container runtime - Docker,containerd, CRI-O.


### Kubelet
Communicates with the K8 master.An agent that runs on each node in the system, it makes sure that container
described in PodSpecs are running and healthy.

### kube-proxy
kube-proxy maintains network rules on nodes. These network rules allow network communication to your Pods
from network sessions inside or outside of your cluster. The kube-proxy will make changes to iptables to ensure correct routing to pods/services is set up


--- Image Here -----



## Kubernetes Objects (basic abstractions)
 Objects are persistent entites in K8 system and represent cluster state.  
 Which node has what containers and with what resources and what policies govern them(restart, upgrade, fault-tolerance etc)
 
Every K8s object has object **spec** and the object **status**. 
The spec, which you must provide, describes your desired state for the object. 
The status describes the actual state of the object, and is supplied and updated by the Kubernetes system. 
At any given time, the Kubernetes Master (Control Plane) actively manages an object’s actual state to match the desired state you supplied.

Example of a spec - application/deployment.yaml 
```
apiVersion: apps/v1    #version of the K8s API 
kind: Deployment       # what kind of object is this, deployment in this case
metadata:              # metadata like name, namespace etc 
  name: nginx-deployment
spec:                  # desired state of the object
  selector:
    matchLabels:
      app: nginx
  replicas: 2          # tells deployment to run 2 pods matching the template
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.7.9
        ports:
        - containerPort: 80

```
Then using this spec , a deployment can be created as
```
kubectl apply -f https://k8s.io/examples/application/deployment.yaml --record
```

 
Following are K8s objects-
1.Nodes 
2. Pods
3. Service
4. Volume
5. Namespace


## Pods -
A Kubernetes Pod is a group of one or more Containers(such as Docker or rkt), tied together for the purposes of administration and networking. Containers in a pod share same IP and ports.
Pod resources include:
- Shared storage, as Volumes
- Networking, as a unique cluster IP address
- Information about how to run each container, such as the container image version or specific ports to use

Pods are the atomic unit on the Kubernetes platform. When we create a Deployment on Kubernetes, that Deployment creates Pods with containers inside them (as opposed to creating containers directly). 
**Each Pod is tied to the Node where it is scheduled**, and remains there until termination (according to restart policy) or deletion. In case of a Node failure, identical Pods are scheduled on other available Nodes in the cluster.

### Pod Lifecycle methods
Lifecycle
init>PodInitializing>Running>Terminating > Terminated

- init container (if defined)
- post start hook
- any probes -> Liveness Probe, readineess probe
- pre stop hooks
https://github.com/wardviaene/kubernetes-course/blob/master/pod-lifecycle/lifecycle.yaml

## Nodes
A Pod always runs on a Node. A node can have multiple Pods. Each Node is managed by the Master. The Kubernetes master automatically handles scheduling of pods across the Nodes in the cluster based on the resources available on each node. When a node crashes , pods in the node die with it.

## Service
Each Pod in a Kubernetes cluster has a unique IP address, even Pods on the same Node.Although each Pod has a unique IP address, those IPs are not exposed outside the cluster without a Service. Services allow your applications to receive traffic.
They do the load balancing.

A Service in Kubernetes is an abstraction which defines a logical set of Pods and a policy by which to access them.
Services enable a loose coupling between dependent Pods. A Service is defined using YAML (preferred) or JSON, like all Kubernetes objects. The set of Pods targeted by a Service is usually determined by a LabelSelector.
Discovery and routing among dependent Pods (such as the frontend and backend components in an application) is handled by Kubernetes Services.

Services can be exposed in different ways by specifying a type in the ServiceSpec:

1. ClusterIP (default) - Exposes the Service on an internal IP in the cluster. Only reachable from within the cluster.
2. NodePort - Exposes the Service on the same port of each selected Node in the cluster using NAT. Makes a Service accessible from outside the cluster using <NodeIP>:<NodePort>. Superset of ClusterIP.
3. LoadBalancer - Creates an external load balancer in the current cloud (if supported) and assigns a fixed, external IP to the Service. Superset of NodePort.example AWS ELB
4. ExternalName - Exposes the Service using an arbitrary name (specified by externalName in the spec) by returning a CNAME record with the name. No proxy is used. This type requires v1.7 or higher of kube-dns(dns addon)


By default service can run only on port range 30000- 32767.

## Kubernetes Higher level abstractions(rely on controllers)

1. Deployment
2. DaemonSet
3. StatefulSet
4. ReplicaSet
5. Job


For example, a Kubernetes Deployment is an object that can represent an application running on your cluster. 
When you create the Deployment, you might set the Deployment spec to specify that you want three replicas of the application to be running. The Kubernetes system reads the Deployment spec and starts three instances of your desired application–updating the status to match your spec. If any of those instances should fail (a status change), the Kubernetes system responds to the difference between spec and status by making a correction–in this case, starting a replacement instance.

-----------
For AWS you can use an external LoadBalancer to route the traffic to correct pods in kubernetes. In kubernetes terms this is equivalent to creating a service with type = Loadbalancer.

## Ingress

Ingress exposes HTTP and HTTPS routes from outside the cluster to services within the cluster. Traffic routing is controlled by rules defined on the Ingress resource.
***You must have an ingress controller to satisfy an Ingress. Only creating an Ingress resource has no effect.You may need to deploy an Ingress controller such as ingress-nginx.

On cloud providers you can use Ingress controller to reduce the cost of your Load Balancers.We can use 1 LB to capture all teh traffic and send it to Ingress controller, the ingress controller will then route the traffic to different applications based on http rules. 


**Alternative of LoadBalancer and NodePort


Use Service.Type=LoadBalancer
Use Service.Type=NodePort

## Deployments, demonsets, statefulsets, ReplicationController
### Deployments 
Deployments manage stateless services running on your cluster (as opposed to for example StatefulSets which do manage stateful services). Their purpose is to keep a set of identical pods running and upgrade them in a controlled way. For example, if you say 5 replica's over 3 node then some nodes have more than one replica of your app running. ReplicationController old way of doing Deployments.
### DaemonSets
DaemonSets manage groups of replicated Pods. However, DaemonSets attempt to adhere to a one-Pod-per-node model, either across the entire cluster or a subset of nodes. Daemonset will not run more than one replica per node.
Another advantage of using Daemonset is, if you add a node to the cluster then Daemonset will automatically spawn pod on that node, which deployment will not do.
DaemonSets are useful for deploying ongoing background tasks that you need to run on all or certain nodes, and which do not require user intervention. Examples of such tasks include storage daemons like ceph, log collection daemons like fluentd, and node monitoring daemons like collectd
Also when a node is remove, its pod will not be rescheduled in another node.

Typical Use cases
- Logging Aggregators
- Load Balancers, reverse proxies, Api gateways
- Monitong 

Lets take example you mentioned in question, why coredns is deployment and kube-proxy is daemonset?
```
kubectl get daemonSets --namespace=kube-system
kubectl get deployments --namespace=kube-system
```
The reason behind that is kube-proxy is needed on every node in cluster to run IP tables so that every node can access every pod no matter on which node it resides. Hence, when we make kube-proxy a daemonset and another node is added to cluster at later time kube-proxy is automatically spawned on that node.
Kube-dns responsibility is to discover the service IP using its name and even one replica of kube-dns is enough to resolve the service name to its IP and hence we make kube-dns a deployment because we don't need kube-dns on every node.

### ReplicaSet
ReplicaSet ensures that a specified number of pod replicas are running at any given time. However, a Deployment is a higher-level concept that manages ReplicaSets and provides declarative updates to Pods along with a lot of other useful features. Use Deployment instead of replicaset.

### StatefulSets
Like a Deployment, a StatefulSet manages Pods that are based on an identical container spec. Unlike a Deployment, a StatefulSet maintains a sticky identity for each of their Pods. These pods are created from the same spec, but are not interchangeable: each has a persistent identifier that it maintains across any rescheduling.
example, Cassandra clusters, ElasticSearch Clusters
A statefulset will also allow you to order startup and teardown.
StatefulSets are valuable for applications that require one or more of the following.
-Stable, unique network identifiers.
-Stable, persistent storage.
-Ordered, graceful deployment and scaling.
-Ordered, automated rolling updates.

The pods have a particular name and have their own storage, pods die but storage does not. Pods when the come back online will have the same name as the one that died. Example Cassandra cluster which has a master as described here
Example - https://kubernetes.io/docs/tutorials/stateful-application/cassandra/
This needs a larger minikube ```minikube start --memory 8192 --cpus=4```


### Autoscaling (UP and Down) pods
Horizontal pods autoscaler yml below. This will scale your initial configuration of pods to a max of 10 if your cpu utilization goes above 50%, So if you have provisioned 200m, then when CPU util reaches 100m, it starts auto scaling . If your cpu util goes zero, it will bring the replicas to just 1 instance running.

```
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: hpa-example-autoscaler
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: your-deployment-name
  minReplicas: 1
  maxReplicas: 10
  targetCPUUtilizationPercentage: 50
```

#### Fault Tolerance in Master
You can have multiple master nodes with each having their own etcd database which will store the cluster state. In addition the cluster state can also be stored in S3 Bucket and if the master and the associated volumes go down, the S3 backup can be used to bring back the cluster.
