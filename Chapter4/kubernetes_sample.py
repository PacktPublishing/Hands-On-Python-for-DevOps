from kubernetes import client, config

# Load Kubernetes configurations
config.load_kube_config()

# Create a Kubernetes client
api = client.CoreV1Api()

# Define namespaces
namespaces = ['mynamespace1', 'mynamespace2']

# Create namespaces
for namespace in namespaces:
    namespace_client = client.V1Namespace(metadata=client.V1ObjectMeta(name=namespace))
    api.create_namespace(namespace_client)

# Create a Kubernetes networking V1 API client
networking_api = client.NetworkingV1Api()

for namespace in namespaces:
    # Define the Network Policy manifest
    network_policy_manifest = {
        "apiVersion": "networking.k8s.io/v1",
        "kind": "NetworkPolicy",
        "metadata": {
            "name": "block-external-traffic",
            "namespace": namespace
        },
        "spec": {
            "podSelector": {},
            "policyTypes": ["Ingress"]
        }
    }

    # Create the Network Policy
    networking_api.create_namespaced_network_policy(namespace=namespace, 
                                                    body=network_policy_manifest)
