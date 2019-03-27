# Main Kubernetes Commands

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
