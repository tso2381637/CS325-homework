def num_inversions(a):
	count = 0
	count += merge_count(a)[1]
	print(count)

def merge_count(a):
	if len(a)==1:
		return [a,0]
	else:
		count = 0
		left = merge_count(a[:len(a)/2])
		right = merge_count(a[len(a)/2:])
		count += left[1] + right[1]
		i, j = 0, 0
		merged = []
		while(i<len(left[0]) and j<len(right[0])):
			if left[0][i] <= right[0][j]:
				merged.append(left[0][i])
				i = i+1
			else:
				count += 1
				merged.append(right[0][j])
				j = j+1
		
		merged += left[0][i:]
		merged += right[0][j:]
		return [merged,count]

num_inversions([4, 1, 3, 2])

num_inversions([2, 4, 1, 3])

num_inversions([4, 2, 5, 1, 6, 3])