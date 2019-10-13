import bisect 


def find(a,t,k):

	pivot = bisect.bisect_right(a,t)
	i = pivot - 1
	j = pivot
	result = []
	while i>=0 and j < len(a) and k>0:
		if abs(a[i] - t) <= abs(a[j] - t):
			result.append(i)
			i-=1	
			k-=1		
		elif abs(a[i] - t) > abs(a[j] - t):
			result.append(j)
			j+=1
			k-=1

	if k>0:
		if j==len(a):
			while(k):
				result.append(i)
				i-=1
				k-=1
		else:
			while(k):
				result.append(j)
				j+=1
				k-=1
	
	result.sort()
	result = [a[i] for i in result]
	return result


