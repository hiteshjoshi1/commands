# Create a new cluster using eksctl

1. Create a AWS CMK first for the EKS cluster to use when encrypting your Kubernetes secrets:

we  first have to create AWS KMS Custom Managed key (CMK)

```
aws kms create-alias --alias-name alias/eksworkshop --target-key-id $(aws kms create-key --query KeyMetadata.Arn --output text)
```

then describe to get the KEY's ARN.
```
export MASTER_ARN=$(aws kms describe-key --key-id alias/eksworkshop --query KeyMetadata.Arn --output text)
```

Also add to bash profile
```
echo "export MASTER_ARN=${MASTER_ARN}" | tee -a ~/.bash_profile
```
export AWS_REGION=ap-southeast-1

Now using MASTER_ARN and AWS_REGION, we create our cluser as follows

```
cat << EOF > eksworkshop.yaml
---
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: eksworkshop-eksctl
  region: ${AWS_REGION}

managedNodeGroups:
- name: nodegroup
  instanceType: t2.micro 
  desiredCapacity: 3
  iam:
    withAddonPolicies:
      albIngress: true

secretsEncryption:
  keyARN: ${MASTER_ARN}
EOF
```

Now create the cluster using the config above
```
eksctl create cluster -f eksworkshop.yaml
```


