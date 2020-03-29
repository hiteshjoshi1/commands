# Istio

Istio config is Kubernetes CRD(Custom Resource Definition).

Control pane components -

## Pilot -

1. service discovery for the Envoy sidecars
2. traffic management for intelligent routing(A/B test, canary rollouts)
3. Resilency (Timeouts, retries, circuit breakers)

## Citadel

TLS certs
For service to service and end-user authentication with built-in identity and credential management.

## Galley

Galley is Istio’s configuration validation, ingestion, processing and distribution component.

Data plane component -

## Envoy proxy -

Attached to every microservices. These form the service mesh in Istio.

Envoy proxies are deployed as sidecars to services, logically augmenting the services with Envoy’s many built-in features, for example:

1. Dynamic service discovery
2. Load balancing
3. TLS termination
4. HTTP/2 and gRPC proxies, websocket
5. Circuit breakers
6. Health checks
7. Staged rollouts with %-based traffic split
8. Fault injection
9. Rich metrics
10. Rate limiting

Istio maintains an internal service registry containing the set of services, and their corresponding service endpoints, running in a service mesh. Istio uses the service registry to generate Envoy configuration. Most services are automatically added to the registry by Pilot adapters that reflect the discovered services of the underlying platform (Kubernetes, Consul, plain DNS).

Traffic Management ApI Resources -

- Virtual services
- Destination rules
- Gateways
- Service entries
- Sidecars

### Virtual Services

virtual services, destination rules are key routing features.
Without virtual services, Envoy distributes traffic using round-robin load balancing between all service instances
Each virtual service consists of a set of routing rules that are evaluated in order, letting Istio match each given request to the virtual service to a specific real destination within the mesh.
Example, you can do a canary deployment using a virtual service using Istio -
90 % of traffic to v1 of an application
10 % of traffic to v2 of an application

Traffic can be routed based on headers, and routing rules in service are evaluated top down.
A default rule should be provided, if no else match.

### Destination Rules

Virtual services as how you route your traffic to a given destination, and then you use destination rules to configure what happens to traffic for that destination.

Load Balancing using detination rules-
Example - 5 replicas of a service exists
How does load is balanced between them?
By default it is round robin.
But using detination rule , you can configure to

- Random: Requests are forwarded at random to instances in the pool.
- Weighted: Requests are forwarded to instances in the pool according to a specific percentage.
  – Least requests: Requests are forwarded to instances with the least number of requests.
  etc

### Gateways

Manage inbound and outbound traffic to your service mesh.
Gateway configuration are applied to standalone envoy proxies that are running along the edge of the mesh, rather than sidecar envoy proxies running alongside your service worloads.
Gateways are primarily used to manage ingress traffic, but you can also configure egress gateways. An egress gateway lets you configure a dedicated exit node for the traffic leaving the mesh, letting you limit which services can or should access external networks.
You can also use a gateway to configure a purely internal proxy.

Istio provides some preconfigured gateway proxy deployments (istio-ingressgateway and istio-egressgateway)

### Service Entries

You use a service entry to add an entry to the service registry that Istio maintains internally. After you add the service entry, the Envoy proxies can send traffic to the service as if it was a service in your mesh.

This service would be apart from the service that are added by the Pilot.
Service Entrries allow you to manage traffic for services running outside the mesh - example

- Redirect and forward traffic for external destinations, such as APIs consumed from the web, or traffic to services in legacy infrastructure.
- Define retry, timeout, and fault injection policies for external destinations.
- Run a mesh service in a Virtual Machine (VM) by adding VMs to your mesh.
- Logically add services from a different cluster to the mesh to configure a multicluster Istio mesh on Kubernetes.

By default, Istio configures the Envoy proxies to passthrough requests to unknown services. However, you can’t use Istio features to control the traffic to destinations that aren’t registered in the mesh.

You can configure virtual services and destination rules to control traffic to a service entry in a more granular way, in the same way you configure traffic for any other service in the mesh. for example to do mutual TLS.

istioctl manifest apply --set profile=demo

kubectl label namespace default istio-injection=enabled

kubectl create -f <(istioctl kube-inject -f helloworld-tls.yaml)
kubectl create -f helloworld-tls-legacy.yaml

export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].nodePort}')
export SECURE_INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="https")].nodePort}')

Great explaination
https://software.danielwatrous.com/istio-ingress-vs-kubernetes-ingress/

\*\* Note-
When using an IngressController, traffic is routed to a Service, which load balances traffic across available Pods.
However, in the case of the Istio Ingress Gateway, the kubernetes Service is only used to get a list of endpoints (Pods). Requests are then send directly to the Envoy proxy in the Pod, bypassing the Service.

Same goes for Egress traffic, which is routed through the envoy proxy and hence can be managed.
