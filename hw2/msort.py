def mergesort(a):
	if len(a)==1:
		return a
	else:		
		left = mergesort(a[:len(a)/2])
		right = mergesort(a[len(a)/2:])
		i, j = 0, 0
		merged = []
		while(i<len(left) and j<len(right)):
			if left[i] <= right[j]:
				merged.append(left[i])
				i = i+1
			else:
				merged.append(right[j])
				j = j+1
		
		merged += left[i:]
		merged += right[j:]

		return merged



print(mergesort([4, 2, 5, 1, 6, 3,7]))
