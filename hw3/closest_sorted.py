import bisect 


def find(a,t,k):

	pivot = bisect.bisect_right(a,t)

	i = pivot - 1
	j = pivot
	result = [None] * len(a)
	while i>=0 and j < len(a):
		if abs(a[i] - t) <= abs(a[j] - t) and k>0:
			result[i] = 1
			i-=1	
			k-=1		
		elif abs(a[i] - t) > abs(a[j] - t) and k>0:
			result[j] = 1
			j+=1
			k-=1
	while(k>0):
		if j==len(a):
			result[i] = 1
			i-=1
			k-=1
		else:
			result[j+pivot]=1
			j+=1
			k-=1
	for index,value in enumerate(result):
		if value == 1:
			yield(a[index])

