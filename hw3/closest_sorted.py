import bisect 


def find(a,t,k):

	pivot = bisect.bisect_right(a,t)
	i = pivot - 1
	j = pivot
	result = [None] * len(a)
	result2 = []
	while i>=0 and j < len(a) and k>0:
		if abs(a[i] - t) <= abs(a[j] - t):
			result[i] = 1
			i-=1	
			k-=1		
		elif abs(a[i] - t) > abs(a[j] - t):
			result[j] = 1
			j+=1
			k-=1

	if k>0:
		if j==len(a):
			while(k):
				result[i]=1
				i-=1
				k-=1
		else:
			while(k):
				result[j]=1
				j+=1
				k-=1
	for index,value in enumerate(result):
		if value == 1:
			result2.append(a[index])

	return result2



