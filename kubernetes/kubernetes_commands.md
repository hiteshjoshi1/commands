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


Now you can create deployments. for example
```
kubectl create deployment mydeployment --image=gcr.io/google-samples/kubernetes-bootcamp:v1
```
OR

```
kubectl create deployment nginx --image=nginx
```
You can create a Service at the same time you create a Deployment by using --expose in kubectl.


Describe all Pods
```
kubectl describe pods
```
Get a pod logs
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

Service -
By default, the Pod is only accessible by its internal IP address within the Kubernetes cluster. To make a Container accessible from outside the Kubernetes virtual network, you have to expose the Pod as a Kubernetes Service.


Get all running services
```
kubectl get services
```
-- We have a Service called kubernetes that is created by default when minikube starts the cluster. 

Create a New Service ~
nginx deployment service(Service type - external)
```
kubectl expose deployment nginx --external-ip=$MASTER_IP --port=80 --target-port=80
```
Nodejs example service (Service type - NodePort) With this exposed, you will get response from Nodejs at MinikubeIp:NodePort

```
kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080
```


Scale out a deployment

```
kubectl scale deployment nginx --replicas=6
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

### Expose a deployment as a service -

```
kubectl expose deployment nginx --external-ip=10.96.0.1 --port=80 --target-port=80
```

### Scale a Deployment

```
kubectl scale deployment nginx --replicas=6
```

### Run your own image from DockerHub

```
kubectl run ts-node --image hiteshjoshi1/ts-node:latest
```

### Expose the running service out

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
kubectl config use-context minikube
