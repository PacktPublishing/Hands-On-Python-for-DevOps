from azure.mgmt.containerservice.models import ManagedCluster, ManagedClusterAgentPoolProfile 

resource_group = '<RESOURCE_GROUP_HERE>' 

cluster_name = '<CLUSTER_NAME_HERE>' 

location = '<LOCATION_HERE>' 

 agent_pool_profile = ManagedClusterAgentPoolProfile( 

    name='agentpool', 

    count=3,   

    vm_size='Standard_DS2_v2',  

) 

 aks_cluster = ManagedCluster(location=location, kubernetes_version='1.21.0', agent_pool_profiles = [agent_pool_profile]) 

aks_client.managed_clusters.begin_create_or_update(resource_group, cluster_name, aks_cluster).result() 
