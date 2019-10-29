def bsts(n,bstd=None):


	if bstd == None: bstd={0:1,1:1}

	if n not in bstd:
		result = 0
		for i in range(1,n+1):
			left = bsts(i-1)
			right = bsts(n-i)
			result+=left*right
		bstd[n] = result

	return bstd[n]



print(bsts(5))