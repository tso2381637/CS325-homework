import heapq
def ksmallest(k, a):
	a = list(a)
	result = [-i for i in a[:k]]
	heapq.heapify(result)
	for i in a[k:]:
		if i<-result[0]:
			heapq.heapreplace(result,-i)

	result = [-i for i in result]
	result.reverse()
	return result



#print(ksmallest(3, range(1000000, 0, -1)))

#print(ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7]))