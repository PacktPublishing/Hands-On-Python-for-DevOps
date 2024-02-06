from google.cloud import container_v1 

# Specify your project ID and cluster details 

project_id = "<YOUR_PROJECT_ID>"

zone = "<PREFERRED_ZONE>" 

cluster_name = "<YOUR_CLUSTER>" 

node_pool_name = 'default-pool' 

node_count = 1 

     client = container_v1.ClusterManagerClient() 

  

    # Create a GKE cluster 

    cluster = container_v1.Cluster( 

        name=cluster_name, 

        initial_node_count=node_count, 

        node_config=container_v1.NodeConfig( 

            machine_type='n1-standard-2', 

        ), 

    ) 

    operation = client.create_cluster(project_id, zone, cluster) 
