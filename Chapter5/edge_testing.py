''' the request variable is a json that contains the request headers 
and body'''
def process_request(request):
	'''get all headers'''
	headers = request["headers"]
	''' we're using country in this example, but this is any arbitrary 
	header you choose to pass '''
	request_country = headers["country"]
	''' throw to a function that maps each available server to a country 
	'''
	server = server_map(request_country)
	''' return value from correct server as prescribed by server map '''
	return server_response(server, request)
