# Main Kubernetes Commands

Pods -
A Kubernetes Pod is a group of one or more Containers, tied together for the purposes of administration and networking.

Deployment -
A Kubernetes Deployment checks on the health of your Pod and restarts the Pod’s Container if it terminates. Deployments are the recommended way to manage the creation and scaling of Pods.

```
kubectl create deployment nginx --image=nginx
```

Service -
By default, the Pod is only accessible by its internal IP address within the Kubernetes cluster. To make a Container accessible from outside the Kubernetes virtual network, you have to expose the Pod as a Kubernetes Service.

```
kubectl expose deployment nginx --external-ip=$MASTER_IP --port=80 --target-port=80
```

Scale out a deployment

```
kubectl scale deployment nginx --replicas=6
```

Get All Pods, Services and Deployments
kubectl get all

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

### Create a deployment- example for Nginx

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

Switching between Kubernetes Contexts -


```
kubectl config use-context <context_name>

```
example -
kubectl config use-context minikube




