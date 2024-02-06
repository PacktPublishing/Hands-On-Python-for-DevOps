from google.cloud import binaryauthorization_v1
def sample_create_attestor():
	client = binaryauthorization_v1.BinauthzManagementServiceV1Client()
	attestor = binaryauthorization_v1.Attestor()
	attestor.name = <Enter_attestor_name>
	request = binaryauthorization_v1.CreateAttestorRequest(
		parent=<Enter_parent_value_of_attestor>,
		attestor_id=<Enter_attestor_id>,
		attestor=attestor,
		 )
	client.create_attestor(request=request)
