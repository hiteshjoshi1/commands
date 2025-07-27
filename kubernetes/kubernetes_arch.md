# Kubernetes Architecture

When you deploy Kubernetes, you get a cluster.

A cluster has 2 main components -
1. Kubernetes MASTER : also called a Control Plane (Master): manages global state and scheduling
2. WORKER nodes: run actual application workloads
3. Networking & Storage: interconnect components and persist data

Every cluster has at least one worker node.


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
Kubectl converts the yaml file to JSON and sends the request to kube-apiserver. Validates REST requests, and writes object data to etcd.

### etcd
 A consistent, distributed key–value store holding the cluster’s desired & actual state—a single source of truth. All pod definition is stored in here.
 
### kube-scheduler
Watches for unscheduled Pods and assigns them to nodes based on resource availability, policies, affinity, and constraints.
This is based on various factors such as individual and collective resource requirements, hardware/software/policy constraints, affinity and anti-affinity specifications, data locality, inter-workload interference and deadlines.

### kube-controller-manager
Combines multiple controllers (node, replication, endpoint, service, volume, token controllers, etc.) each continuously reconciling actual vs desired state.

___________________________________

## Kubernetes Worker nodes
Has 3 main parts -
1. Kubelet 
2. kube-proxy - a network proxy which reflect K8s networking service on each node.
3. Container runtime - Docker,containerd, CRI-O.


### Kubelet
A node-level agent that:
1. Registers the node with the control plane / Master
2. Watches Pod specs, ensures containers are started and healthy
3. Periodically sends node and pod status to API server
It makes sure that container described in PodSpecs are running and healthy.

### kube-proxy
kube-proxy maintains network rules on nodes. Manages cluster networking by:
1. Pulling Service & Endpoint info from the API
2. Setting iptables (or ipvs) rules to route Service traffic to corresponding Pods. These network rules allow network communication to your Pods
3. Providing load balancing and DNS-based discovery



![kubernetes Architecture](https://github.com/hiteshjoshi1/commands/blob/master/images/kubernetes_arc.png)


### Key Controller Types & Their Responsibilities
#### 1. Node Controller: 
Monitors node health; if a node becomes unhealthy, it marks it unschedulable, triggering pod rescheduling.
#### 2. Route Controller (cloud-controller-manager): 
Manages cloud-native routing resources like load balancers or DNS entries.
#### 3. ReplicationController: 
Ensures a defined number of Pod replicas are running. Legacy abstraction, **largely superseded by ReplicaSet + Deployments.**
#### 4. Endpoint Controller: 
Maintains Endpoints objects mapping Services to Pod IPs, ensuring accurate routing.
#### 5. Service & Token Controller: 
Manages default ServiceAccounts and token secrets for Pods.
#### 6. Volume Controller: 
Manages lifecycle of volumes—both dynamic provisioning and attachment to Pods.
#### 7. cloud-controller-manager
cloud-controller-manager runs controllers that interact with the underlying cloud providers.
cloud-controller-manager allows the cloud vendor’s code and the Kubernetes code to evolve independently of each other. 

The following controllers have cloud provider dependencies:

1. Node Controller: For checking the cloud provider to determine if a node has been deleted in the cloud after it stops responding
2. Route Controller: For setting up routes in the underlying cloud infrastructure
3. Service Controller: For creating, updating and deleting cloud provider load balancers
4. Volume Controller: For creating, attaching, and mounting volumes, and interacting with the cloud provider to orchestrate volumes


## Kubernetes Objects (basic abstractions)

### 1. Pod
- The smallest deployable unit: one or more containers sharing storage, networking, and lifecycle context.
- Containers in a Pod can communicate via localhost and share volumes.
- Pods contain information about how to run each container, such as the container image version or specific ports to use
- **Each Pod is tied to the Node where it is scheduled**,
### 2. Deployment
Higher-level API that declares desired replica count, update strategy, and Pod spec.

### 3. Node
- A VM or physical machine in the cluster that runs kubelet, kube-proxy, and containers.
- Nodes host Pods and report status to control plane. A node can have multiple Pods. 
- Each Node is managed by the Master.
- The Kubernetes master automatically handles scheduling of pods across the Nodes in the cluster based on the resources available on each node.
- When a node crashes , pods in the node die with it


### 4. Volume
- Defines persistent (or ephemeral) storage mounted into Pods.
- Types include ConfigMap, secret, persistent volumes (PV) with dynamic provisioning.

### 5. Service
- Network abstraction that defines logical set of Pods (via labels) and policies to access them.
- Provides stable IP/DNS and load-balanced traffic routing—even as Pods scale or shift.
- Each Pod in a Kubernetes cluster has a unique IP address, even Pods on the same Node.
- Although each Pod has a unique IP address, those IPs are not exposed outside the cluster without a Service. Services allow your applications to receive traffic.
- The set of Pods targeted by a Service is usually determined by a LabelSelector.
- Discovery and routing among dependent Pods (such as the frontend and backend components in an application) is handled by Kubernetes Services.



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




### Pod Lifecycle methods
Lifecycle
init>PodInitializing>Running>Terminating > Terminated

- init container (if defined)
- post start hook
- any probes -> Liveness Probe, readineess probe
- pre stop hooks
https://github.com/wardviaene/kubernetes-course/blob/master/pod-lifecycle/lifecycle.yaml



### Service types
Services can be exposed in different ways by specifying a type in the ServiceSpec:

1. ClusterIP (default) - Exposes the Service on an internal IP in the cluster. Only reachable from within the cluster.
2. NodePort - Exposes the Service on the same port of each selected Node in the cluster using NAT. Makes a Service accessible from outside the cluster using <NodeIP>:<NodePort>. Superset of ClusterIP.
3. LoadBalancer - Creates an external load balancer in the current cloud (if supported) and assigns a fixed, external IP to the Service. Superset of NodePort.example AWS ELB
4. ExternalName - Exposes the Service using an arbitrary name (specified by externalName in the spec) by returning a CNAME record with the name. No proxy is used. This type requires v1.7 or higher of kube-dns(dns addon)


By default service can run only on port range 30000- 32767.

### Sevice vs Kube-proxy
- Service = abstract API layer (logical grouping, stable address).
- kube‑proxy = mechanism that implements that Service at the node networking level. It ensures traffic to the Service IP is forwarded appropriately

## Kubernetes Higher level abstractions(rely on controllers)

1. Deployment
2. DaemonSet
   Deploys one Pod per (or per-group of) node—ideal for logging agents, kube-proxy itself, or monitoring.
4. StatefulSet
   Manages Pods that require stable identity and persistent storage (e.g. databases, Kafka). Maintains ordered deployment, unique Pod names.
6. ReplicaSet
7. Job

### Deployment vs ReplicaSet
1. You define a Deployment with replicas: 3.
2. Kubernetes creates a matching ReplicaSet (RS) and Pods.
3. On changes (e.g. new image), Deployment creates a new RS and gradually transitions Pods, enabling easy rollback if issues occur.

For example, a Kubernetes Deployment is an object that can represent an application running on your cluster. 
When you create the Deployment, you might set the Deployment spec to specify that you want three replicas of the application to be running. The Kubernetes system reads the Deployment spec and starts three instances of your desired application–updating the status to match your spec. If any of those instances should fail (a status change), the Kubernetes system responds to the difference between spec and status by making a correction–in this case, starting a replacement instance.


## Deployments, demonsets, statefulsets
### 1. Deployments 
Deployments manage stateless services running on your cluster (as opposed to for example StatefulSets which do manage stateful services). Their purpose is to keep a set of identical pods running and upgrade them in a controlled way. For example, if you say 5 replica's over 3 node then some nodes have more than one replica of your app running. ReplicationController old way of doing Deployments.

### 2. DaemonSets
DaemonSets attempt to adhere to a "one-Pod-per-node" model, either across the entire cluster or a subset of nodes. Daemonset will not run more than one replica per node. Another advantage of using Daemonset is, if you add a node to the cluster then Daemonset will automatically spawn pod on that node, which deployment will not do.
DaemonSets are useful for deploying ongoing background tasks that you need to run on all or certain nodes, and which do not require user intervention. 
Use cases
1. Node-level logging or metrics collector: e.g., Fluentd, Prometheus node-exporter, or Filebeat running on every node.
2. Networking agents or security tools: Implementations like Cilium, Istio sidecars, or firewall agents that must reside on each host.
3. Load Balancers, reverse proxies, Api gateways
4. Monitong
5. Kube-proxy is a demonset

#### why coredns is deployment and kube-proxy is daemonset?
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


For AWS you can use an external LoadBalancer to route the traffic to correct pods in kubernetes. In kubernetes terms this is equivalent to creating a service with type = Loadbalancer.

## Ingress
- Ingress is a Kubernetes API resource that defines HTTP/HTTPS routing rules. It lets you expose cluster services via hostnames and paths (e.g. app.sc.com/api → Service A, app.sc.com/auth → Service B)
- Layer over Services to expose HTTP/HTTPS routes externally; managed by an Ingress controller.
Ingress exposes HTTP and HTTPS routes from outside the cluster to services within the cluster. Traffic routing is controlled by rules defined on the Ingress resource.

Key Ingress capabilities include:
1. TLS termination
2. Host-based routing
3. Path-based routing
4. Load balancing across multiple Services  

***You must have an ingress controller to satisfy an Ingress. Only creating an Ingress resource has no effect. You may need to deploy an Ingress controller such as ingress-nginx.


### Ingress Controller
- **An Ingress Controller is a running Kubernetes instance—often a Deployment or DaemonSet—that watches Ingress resources and enforces their routing logic, typically by configuring a reverse proxy or load balancer like NGINX, Traefik, Kong, or HAProxy**
- On cloud providers you can use Ingress controller to reduce the cost of your Load Balancers. We can use 1 LB to capture all the traffic and send it to Ingress controller, the ingress controller will then route the traffic to different applications based on http rules. 


```
apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  name: simple-fanout-example
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: foo.bar.com
    http:
      paths:
      - path: /foo
        backend:
          serviceName: service1
          servicePort: 4200
      - path: /bar
        backend:
          serviceName: service2
          servicePort: 8080
```

## Service vs Ingress vs Ingress controller
- Service defines how Pods communicate internally;
- Ingress defines how external traffic enters;
- Ingress Controller enforces those Ingress rules at network level
Scenario: Suppose a bank wants to serve two applications—app1 and app2—under the same external URL services.bank.com, where:

/api → Service A

/auth → Service B

#### Step 1: Service
- You create two ClusterIP Services inside Kubernetes:
- api-service pointing to Pods of app1
- auth-service pointing to Pods of app2
These services give stable IPs within the cluster for internal communication only.

#### Step 2: Ingress Resource
- Define an Ingress object with rules:
- Requests to services.bank.com/api → api-service
- Requests to services.bank.com/auth → auth-service
- Specifies TLS termination and routing logic in YAML, but does nothing on its own.

#### Step 3: Ingress Controller
- Deploy an Ingress Controller (e.g. ingress-nginx) as a deployment or DaemonSet.
- It watches Ingress resources and configures a reverse proxy (like NGINX) to enforce routing.
- It exposes port 80/443, handles TLS, headers, routing to backend services.
- Multiple HTTP services exposed under one IP/domain via path-based or hostname-based routing.
- Unified TLS termination, dynamic routing, and canary deployments.


Summary:
- Service: internal abstraction to load balance Pods.
- Ingress : A Kubernetes API resource that defines HTTP/HTTPS routing rules (based on hostnames, paths, TLS, etc.) to Services inside the cluster.
- Ingress Controller: Implements Ingress rules by configuring a reverse proxy (e.g., ingress-nginx, Traefik). It handles routing, TLS termination, and load balancing at Layer 7.



### Service type: LoadBalancer 
- In cloud environments (AWS EKS, Azure AKS), a Service declared as type: LoadBalancer triggers the cloud provider to provision a native load balancer.
- Kubernetes populates EXTERNAL-IP with the public IP from the cloud LB resource.
- Incoming traffic is routed via the Load Balancer directly into your cluster and distributed to Pods through NodePorts and kube-proxy.
- Exposes a single Service externally by provisioning a cloud-provider load balancer (e.g. AWS ELB, Azure LB), assigning a dedicated external IP to that Service. Routes all traffic (TCP/UDP) to Pods set by the Service selector.

### Service type : Nodeport
- Exposes a fixed port (e.g. 32456) on every node's IP address.


Use Service.Type=LoadBalancer
Use Service.Type=NodePort



