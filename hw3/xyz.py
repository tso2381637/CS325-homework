def find(a):


	a.sort()
	for element in a:
		i = 0
		j = len(a)-1
		while(i!=j):
			if a[i] + a[j] == element:
				print(a[i], a[j], element)
				i+=1
			elif a[i] + a[j] > element:
				j-=1
			else :
				i+=1



find([1, 4, 2, 3, 5])