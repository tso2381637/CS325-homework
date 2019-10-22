import random
def qselect(k,a):
    if a == [] or k>len(a) or k==0:
        return []
    else:
        i=random.randint(0,len(a)-1)
        a[0],a[i]=a[i],a[0]
        pivot=a[0]
        left = [x for x in a if x < pivot ]


        splitP=len(left)
        if splitP==k-1:
            return pivot
        
        elif splitP>k-1:
            return qselect(k,left)
        
        else:
            right = [x for x in a[1:] if x >= pivot]
            return qselect(k-(splitP+1),right)
def nbesta(a,b):
	result = []
	for i in a:
		for j in b:
			result.append((i+j,i,j))

	result.sort()
	return [ (j,k) for i,j,k in result[:len(a)]]

def nbestb(a,b):
	result = []
	for i in a:
		




if __name__ == "__main__":
	a, b = [4, 1, 5, 3], [2, 6, 3, 4]
	print(nbesta(a,b))