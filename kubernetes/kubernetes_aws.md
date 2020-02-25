# Kubernetes on AWS

1. EKS - Managed service - costly
2. Kops - create a cluster on your own - not managed


----------------------------------------------
## Creating a cluster in  AWS using Kops

### One time setup
1.Install kops
```
brew update && brew install kops
```

2.Install Pythin pip
python-pip

3.Install awscli
```
pip install awscli
```

4. Create a kops user in AWS IAM, Give Admin access

5. Create an S3 bucket to store cluster state

6. Need a domain- buy one
7. Create a subdomain in Route 53 - Route 53 - DNS Management
8. Add NS records to your main domain
9. setup your aws user in terminal
```
aws configure
```
----------------------------------------------------

## Create Cluster using kops

### Command that will similuate creating a cluster
```
kops create cluster --name=subdomain.domain.com --state=s3://kops-state-hitesh --zones=ap-southeast-1a --node-count=2 --node-size=t2.micro --master-size=t2.micro --dns-zone=subdomain.domain.com
```
where kops-state-hitesh  is the bucket name. 
This will create a 3 node cluster (1 master and 2 worker nodes).

### Run / create actual cluster
```
kops update cluster --name subdomain.domain.com --state=s3://kops-state-hitesh --yes
```

### Get cluster state
```
kops get cluster --state=s3://kops-state-hitesh
```

### Create a deployment - Actual pod creation
```
kubectl run hello-minikube --image=k8s.gcr.io/echoserver:1.4 --port=8080
```

### Expose the service
```
kubectl expose deployment hello-minikube --type=NodePort
```
To check exposed service
```
kubectl get service
```

### Delete a cluster if needed
```
kops delete cluster --name subdomain.domain.com --state=s3://kops-state-hitesh --yes
```

example - create a pod
```
kubectl create -f first-app/helloworld.yml
```
If you want to create a Loadbalncer using kubernetes service
```
aws iam create-service-linked-role --aws-service-name "elasticloadbalancing.amazonaws.com" 
```
Expose it via Loadbalancer- This will create a LB in Aws

kubectl create -f first-app/helloworld-service.yml  
```


```


How does the AWS LoadBalancer routes traffic to the correct pod?
AWS loadbalancer uses NodePort that is exposed on all non master nodes.




