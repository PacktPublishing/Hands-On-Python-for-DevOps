import multiprocessing
''' Get list and return sum '''
def get_sum(numerical_array):
	''' return sum of array '''
	return sum(numerical_array)
	'''method that calls sum method to get total sum for 1 million records 
	'''
def get_total_sum(full_array):
	''' Initialize 4 processors '''
	pool = multiprocessing.Pool(processes=4)
	''' List of sums in 10,000 number blocks '''
	sum_list = []
	''' Get 10,000 values at a time for sum out of 1,000,000 '''
	for i in range(0, count(full_array)/10000):
		sum_array = full_array[i*10000:(i+1)*10000]
		'''Make an array of 10,000 length arrays '''
		sum_list.append(sum_array)
	''' Get final array of sums of each 10,000 value array '''
	final_array_list = pool.map(get_sum, sum_list)
	''' Get one final sum of all these elements '''
	return sum(final_array_list)
