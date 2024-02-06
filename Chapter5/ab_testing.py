''' get request from user '''
def process_request(request):
	''' get a random number between 1 and 10 '''
	num = random.randrange(1,10)
	''' conditionally return site containing special feature '''
	if num<=2:
		return special_response(request)
	else:
		return regular_response(request)
