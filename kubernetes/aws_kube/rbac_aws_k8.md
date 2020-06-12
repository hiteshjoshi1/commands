# RBAC- How to specify role base access to cluster in AWS

We will create a new namespace and a new user.
And give user access only to resources in this new namespace. We can specify the granularity of access.
In this example, we will give get, list and watch access to the user.

### Get the Auth configmap from the cluster - This only works with cluster created with eksctl
```
kubectl get configmap -n kube-system aws-auth -o yaml > aws-auth.yaml
```

###  Create a new Account  in Aws -
```
aws iam create-user --user-name rbac-user
aws iam create-access-key --user-name rbac-user | tee /tmp/create_output.json
```

###  Add the newly created account to the configmap (aws-auth.yaml)
This will create a new K8 user and map it to AWS User that we created above.

```
cat << EoF >> aws-auth.yaml
data:
  mapUsers: |
    - userarn: arn:aws:iam::${ACCOUNT_ID}:user/rbac-user
      username: rbac-user
EoF
```

###  Apply the new configmap
```
kubectl apply -f aws-auth.yaml
```

Now the K8 user is created but it has no permissions - You can test by doing

###  Set the new user to your aws cli , with

```
export AWS_SECRET_ACCESS_KEY=<New user access key>
export AWS_ACCESS_KEY_ID=<New user access Id>
```

Now you can check access with
```
kubectl get pods -n rbac-test
```

To give access, return back to admin user
```
unset AWS_SECRET_ACCESS_KEY
unset AWS_ACCESS_KEY_ID
```

###  Then the admin should create a Role and RoleBinding as follows

create a role, let's call it pod-reader

```
cat << EoF > rbacuser-role.yaml
kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  namespace: rbac-test
  name: pod-reader
rules:
- apiGroups: [""] # "" indicates the core API group
  resources: ["pods"]
  verbs: ["list","get","watch"]
- apiGroups: ["extensions","apps"]
  resources: ["deployments"]
  verbs: ["get", "list", "watch"]
EoF
```

###  RoleBinding - binds the pod-reader role with rbac-user created previously
```
cat << EoF > rbacuser-role-binding.yaml
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: read-pods
  namespace: rbac-test
subjects:
- kind: User
  name: rbac-user
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
EoF
```

###  Apply the role and role binding
```
kubectl apply -f rbacuser-role.yaml
kubectl apply -f rbacuser-role-binding.yaml
```

Now you can switch back to newly created user in aws cli and run kubectl queries in rbac-test namespace.


Main Tutorial - https://eksworkshop.com/beginner/090_rbac/
