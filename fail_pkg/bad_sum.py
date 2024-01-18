# This fun provides sum of list
def bad_sum(list):
	total = 0
	for item in list:
		total = item + total
	return total
