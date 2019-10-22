import heapq
import time
import random
def kmergesort(a,k):
	if len(a)<k:
		#print(a)
		a.sort()
		return a
	else:
		#print('enter:',a)
		result = []
		la = len(a)
		k_array = [0] * k
		min_margin = [(len(a)//k)*i for i in range(0,k)]
		max_margin = [(len(a)//k)*i for i in range(1,k)]
		max_margin.append(len(a))
		for i in range(0,k):
			a[min_margin[i]:max_margin[i]] = kmergesort(a[min_margin[i]:max_margin[i]],k)
		#print(a)
		while(True):
			heap = []
			for j in range(0,k) : 
				if(min_margin[j]+k_array[j]<max_margin[j]): 
					#print('append:',(a[min_margin[j]+k_array[j]],j))
					heap.append((a[min_margin[j]+k_array[j]],j))

			if heap==[]:
				break
			heapq.heapify(heap)
			#print('heap:',heap)

			poped = heapq.heappop(heap)
			result.append(poped[0])
			k_array[poped[1]]+=1
		#print('result:',result)
		return result


arr = [4,1,5,2,6,3,7,0]
print(kmergesort(arr,3))
arr = [4,1,5,2,6,3,7,0]
arr.sort()
print(arr)

# n = 1000
# k=2
# while(n<16000):
# 	a = random.sample(list(range(0,n)),n)
# 	start = time.time()
# 	kmergesort(a,k)
# 	print('kmergesort',n,time.time()-start)
# 	a = random.sample(list(range(0,n)),n)
# 	start = time.time()
# 	a.sort()
# 	print('sort',n,time.time()-start)
# 	n*=2
# 	k*=k