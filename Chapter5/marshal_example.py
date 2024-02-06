import marshal
''' function to decode bytes '''
def decode_bytes(data):
	''' Load binary data into readable data with marshal '''
	result = marshal.loads(data)
	''' Return raw data '''
	return result
