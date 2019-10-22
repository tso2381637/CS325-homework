import heapq
def ksmallest(k, a):
	a = list(a)
	result = a[:k]
	heapq._heapify_max(result)
	result.sort(reverse=True)
	for i in a[k:]:
		if i<result[0]:			
			result = result[1:]
			for j in range(0,len(result)):
				if j==len(result)-1:
					result.insert(j+1,i)
					break
				elif i<=result[j] and i>=result[j+1]:
					result.insert(j+1,i)

	result.reverse()
	return result



#print(ksmallest(3, range(1000000, 0, -1)))

#print(ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7]))

#print(ksmallest(6, [10, 2, 9, 3, 7, 8, 11, 9, 3, 7, 8, 11, 8, 11, 5, 7]))

#print(ksmallest(10, [10, 2, 9, 3, 7, 3, 9, 3, 7, 8, 11, 8, 11, 5, 7]))