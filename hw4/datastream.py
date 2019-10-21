import heapq
def ksmallest(k, a):
	a = list(a)
	result = a[:k]
	heapq.heapify(result)
	for i in a[k:]:
		if i<result[k-1]:
			result[k-1] = i
			result.sort()

	return result



#print(ksmallest(3, range(1000000, 0, -1)))

#print(ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7]))

#print(ksmallest(6, [10, 2, 9, 3, 7, 8, 11, 9, 3, 7, 8, 11, 8, 11, 5, 7]))

