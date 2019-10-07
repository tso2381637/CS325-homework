def longest(a):
	left = count_deepth(a[0])
	right = count_deepth(a[2])
	return max([left[1],right[1],left[0]+right[0]])

def count_deepth(a):
	if len(a)==1:
		return [1,0]
	elif len(a)==0:
		return [0,0]
	else:
		count = 0
		left = count_deepth(a[0])
		right = count_deepth(a[2])
		count += max(left[0],right[0]) + 1
		longest = max([left[1],right[1],count])
		return [count,longest]


