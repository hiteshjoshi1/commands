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
 etcd is a key-value store, and is used as backing store of all cluster data.
 
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
from network sessions inside or outside of your cluster.


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

## Nodes
A Pod always runs on a Node. A node can have multiple Pods. Each Node is managed by the Master. The Kubernetes master automatically handles scheduling of pods across the Nodes in the cluster based on the resources available on each node.


## Kubernetes Higher level abstractions(rely on controllers)

1. Deployment
2. DaemonSet
3. StatefulSet
4. ReplicaSet
5. Job


For example, a Kubernetes Deployment is an object that can represent an application running on your cluster. 
When you create the Deployment, you might set the Deployment spec to specify that you want three replicas of the application to be running. The Kubernetes system reads the Deployment spec and starts three instances of your desired application–updating the status to match your spec. If any of those instances should fail (a status change), the Kubernetes system responds to the difference between spec and status by making a correction–in this case, starting a replacement instance.

-----------
Services
Ingresses
Ingress Controllers (example NGINX Ingress controller)
------------


