from collections import defaultdict
from heapq import heappush, heappop, heapify
allowed = set(['AU', 'UA', 'CG', 'GC', 'GU', 'UG'])
def best(x):

	def _best(i, j):

		if(i, j) in opt:
			return opt[i, j]
		curr = 0
		for k in range(i,j):
			if x[k] + x[j] in allowed:
				if _best(i,k-1) + _best(k+1,j-1) + 1 > curr:
					curr = _best(i,k-1) + _best(k+1,j-1) + 1
					back[i, j] = k

		if _best(i,j-1) > curr:
			curr = _best(i,j-1)
			back[i, j] = -1

		opt[i, j] = curr
		return curr

	def solution(i, j):
		if i == j:
			return '.'
		if i > j:
			return ''
		k = back[i,j]
		if k == -1:
			return '%s.' % solution(i,j-1)
		else:
			return solution(i, k-1) + '(%s)' % solution(k+1,j-1)

	opt = defaultdict(int)
	n = len(x)
	back = {}
	for i in range(n):
		opt[i, i] = 0
		opt[i, i-1] = 0

	return _best(0, n-1),solution(0, n-1)

def total(x):

	def _total(i, j):

		if(i, j) in count:
			return count[i, j]
		curr = 0
		for k in range(i,j):
			if x[k] + x[j] in allowed:
				curr += _total(i,k-1) * _total(k+1,j-1)
			
				
 			
		curr += _total(i,j-1)
			
		#print(i,j,count[i,j])
		count[i, j] = curr

		return curr

	
	count = defaultdict(int)
	n = len(x)
	for i in range(n):
		count[i,i] = 1
		count[i,i-1] = 1
		

	# _total(0,n-1)[1]
	# print(opt)
	
	#print(count)
	return _total(0,n-1)

def kbest(x, k):
	
	
	
	def _kbest(i,j):
		
		
		def trypush_binary(s,p,q):
			if p < len(topk[i,s]) and q <len(topk[s+1,j]) and (s,p,q) not in visted:
				heappush(h,(-(topk[i,s][p][0] + topk[s+1,j][q][0]),(s,p,q)))
				visted.add((s,p,q))

		def trypush_unary(p):			
			if p<len(topk[i+1,j-1]):
				heappush(h,(-(topk[i+1,j-1][p][0]+1),(p,)))
		if (i, j) in topk:
			#print(i,j)
			return topk[i,j]
		
		h,visted = [],set()
		
		for s in range(i,j):
			
			_kbest(i,s)
			_kbest(s+1,j)
			#print(i,j,s,topk[i,s-1],topk[s+1,j-1])
			h.append((-(topk[i,s][0][0] + topk[s+1,j][0][0]), (s,0,0)))
			
		heapify(h)
		if x[i] + x[j] in allowed:
			_kbest(i,j-1)
			trypush_unary(0)

		for _ in range(k):
			if h == []:
				break
			score, indices= heappop(h)
			try:
				s,p,q = indices
				if (-score,topk[i,s][p][1]+topk[s+1,j][q][1]) not in topk[i,j]:
					topk[i,j].append((-score,topk[i,s][p][1]+topk[s+1,j][q][1]))	
					trypush_binary(s,p+1,q)
					trypush_binary(s,p,q+1)
			except:
				p = indices[0]
				if (-score,"(%s)" % topk[i+1,j-1][p][1]) not in topk[i,j]:
					topk[i,j].append((-score,"(%s)" % topk[i+1,j-1][p][1]))
				#print(i,j,topk[i,j])
					trypush_unary(p+1)
		#print(i,j,topk[i,j])
		

	topk = defaultdict(list)
	n = len(x)
	for i in range(n):
		topk[i,i] = [(0,'.')]
		topk[i,i-1] = [(0,'')]

	#print(topk)
	_kbest(0,n-1)

	return topk[0,n-1]


if __name__ == '__main__':
	
	# print(best('ACAGU'))
	# print(best('AGGCAUCAAACCCUGCAUGGGAGCG'))
	# print(total('GAUGCCGUGUAGUCCAAAGACUUC'))
	# print(total('ACAGU'))

	print(kbest('ACAGU',6))