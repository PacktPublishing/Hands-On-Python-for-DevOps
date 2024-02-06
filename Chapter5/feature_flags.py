''' get request from user '''
def process_request(request):
	'''get request header with feature flag '''
	header = request["header"]
	feature = header["feature"]
	''' Check if feature flag is turned on, i.e. if it is True or False 
	'''
	if feature:
		return featured_response(request)
	else:
		return normal_response(request)
