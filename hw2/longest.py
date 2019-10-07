def longest(a):
	print(count_deepth(a[0]) + count_deepth(a[2]))

def count_deepth(a):
	if len(a)==1:
		return 1
	elif len(a)==0:
		return 0
	else:
		count = 0
		left = count_deepth(a[0])
		right = count_deepth(a[2])
		count += max(left,right) + 1
		return count

