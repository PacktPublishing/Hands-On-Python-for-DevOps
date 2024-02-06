from google.cloud import container_v1
def sample_update_cluster():
	client = container_v1.ClusterManagerClient()
	request = container_v1.UpdateClusterRequest(
		"desired_node_pool_id": <Node_pool_to_update>,
		"update": {
			"desired_binary_authorization": {
			"enabled": True,
			"evaluation_mode": 2
			}
		}
	 )
	client.update_cluster(request=request)
