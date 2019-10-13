import random
def find(a,target,k):

	x = [abs(round(i-target,2)) for i in a]
	y = [abs(round(i-target,2)) for i in a]
	kest = qselect(k,x)

	result = []
	for i,value in enumerate(y):
		if value<kest and len(result)<=k: 
			result.append(i)
	for i,value in enumerate(y):
		if value==kest and len(result)<=k: 
			result.append(i)
	
	result.sort()
	print([a[i] for i in result][:k])

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


find([4,1,3,2,7,4], 5.2, 2)
find([4,1,3,2,7,4], 6.5, 3)
find([5,3,4,1,6,3], 3.5, 2)
find([4,1,4,2,7,3], 5.2, 2)