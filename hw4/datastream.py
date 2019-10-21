import heapq
def ksmallest(k,a):
	
	result = a[:k]
	heapq._heapify_max(result)
	for i in a[k:]:
		print(result)
		if i<result[0]:
			heapq._heapreplace_max(result,i)
	return result


