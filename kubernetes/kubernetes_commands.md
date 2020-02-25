# Main Kubernetes Commands


## Minikube and tutorial
After installing minikube and kubectl
```
minikube version
```

```
minikube start
```

```
kubectl version
```

```
kubectl cluster-info
```

Get Nodes in the cluster
```
kubectl get nodes
```
This will return minikube , if it is the minikube cluster.


## Deployment

### describe a Deployment
```
kubectl describe deployment
```

### Create a deployment
```
kubectl create deployment mydeployment --image=gcr.io/google-samples/kubernetes-bootcamp:v1
```
OR

```
kubectl create deployment nginx --image=nginx
```

### Scale UP a deployment

```
kubectl scale deployment nginx --replicas=6
```

### Scale down

```
kubectl scale deployments/kubernetes-bootcamp --replicas=2

or

kubectl scale deployment nginx --replicas=3

```

### Describe all Pods
```
kubectl describe pods
```
### Get pod logs
```
kubectl logs <pod-name>
```

Use exec to run commands directly on the pod once the container is up and running
Below command lists the environment variables of a pod.

```
kubectl exec <Pod_name> env
```
**Or start a bash session with a pod
```
kubectl exec -ti $POD_NAME bash
```

### Service -
By default, the Pod is only accessible by its internal IP address within the Kubernetes cluster. To make a Container accessible from outside the Kubernetes virtual network, you have to expose the Pod as a Kubernetes Service. Services do the load balancing.


Get all running services
```
kubectl get services
```
Note - A Service called kubernetes is created by default when minikube starts the cluster. 

### Expose a  Service ~
example nginx deployment service
```
kubectl expose deployment nginx --external-ip=$MASTER_IP --port=80 --target-port=80
```


Or Nodejs example service. With this service exposed, you will get response from Nodejs at MinikubeIp:NodePort

```
kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080
```
This will expose a service named service/kubernetes-bootcamp

### Describe a service
```
kubectl describe services/kubernetes-bootcamp
```
### Delete a service
```
kubectl delete service -l <labelName=labelValue>
```


You can query a pod or service by label
kubectl get pods -l <labelName=labelValue>
```
kubectl get pods -l app=v1
```
or
```
kubectl get services -l <labelName=labelValue>
```

Get All Pods, Services and Deployments

```
kubectl get all
```

Delete a Deployment and Service

```
kubectl delete deployment.apps/nginx  service/kubernetes
```

Where deployment.apps/nginx is the name of deployment
Where service/kubernetes is the name of the Kubernetes service

### Run the container - if you are on GCE

gcloud container clusters create k0 --zone asia-south1-a

### Get running pods

```
kubectl get pods
```

### Start Nginx service from a VM

```
kubectl run nginx --image=nginx:1.10.0
```

### Create a deployment- example for Nginx -

```
kubectl create deployment nginx --image=nginx
```

### Expose a deployment as a service on a certain port -

```
kubectl expose deployment nginx --external-ip=10.96.0.1 --port=80 --target-port=80
```


## See a replica set
```
kubectl get rs
```
## Scale the Deployments in the replica set
```
kubectl scale deployment nginx --replicas=6
```

### To Update a deployment to a new image
```
kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=jocatalin/kubernetes-bootcamp:v2
```

To see rollout status after the update or rollback command above
```
kubectl rollout status deployments/kubernetes-bootcamp
```

To see current image version of the app
```
kubectl describe pods
```

To rollback a rollout 
```
kubectl rollout undo deployments/kubernetes-bootcamp
```


### Run your own image from DockerHub

```
kubectl run ts-node --image hiteshjoshi1/ts-node:latest
```

### Expose the Deployment out as a service

--type= Loadbalancer will get you an external IP

```
kubectl expose deployments nginx --port 80 --type LoadBalancer

kubectl expose deployments ts-node --port 4100 --type=LoadBalancer --name=ts-node
```

### Get Logs from Kubernetes

```
kubectl logs <Pod_name>
```

### Streaming Logs

```
kubectl logs -f <Pod_name>
```

### Get the Running Services

```
kubectl get services
```

### Get Information on pods

```
kubectl describe pods <podName>
```

Example -
kubectl describe pods ts-node-5578d8d8c-v8vgd

### Port forwarding in K8

```
kubectl port-forward <podName> podPort:machinePort
```

Example
kubectl port-forward ts-node-5578d8d8c-v8vgd 4100:3000

### Intercative Shell inside the pod

```
kubectl exec <podName> --stdin --tty -c <podName> /bin/ssh
```

## Switching between Kubernetes Contexts -

```
kubectl config use-context <context_name>

```

example -
```
kubectl config use-context minikube
```

-----------------------------------------------
### Describe a pod - This will give the port, containerId, Image , image id etc
```
kubectl describe pods nodehelloworld.example.com
```

### Simple Port Forwarding
For quick and dirty testing( ends with Ctrl+C)
```
kubectl port-forward <pod-name> <forwardToPort>:<portonPOD>
kubectl port-forward nodehelloworld.example.com 8081:3000
```

### Creating a service
```
kubectl expose pod nodehelloworld.example.com --type=NodePort --name=nodehelloworld-service 
```
Once the service is created, get the node address. If in cloud, get the master IP address. 
For minikube, get the service URL as
```
minikube service nodehelloworld-service  --url 
```
Another way to do is to get
```
kubectl describe service nodehelloworld-service
```

When we do ```kubectl get service```
The IP address shown is the cluster IP, not accesible to outside or to host machine.
NAME    |                 TYPE   |     CLUSTER-IP  |   EXTERNAL-IP  | PORT(S)      |    AGE
nodehelloworld-service |  NodePort  |  10.109.92.81 |  <none>    |    3000:31784/TCP |   3m38s







