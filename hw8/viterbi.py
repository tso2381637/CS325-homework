from topol import *

def longest(n, edges):

	path = order(n,edges)
	max_num = 0,0
	adjlist = defaultdict(list)
	result = defaultdict(lambda:0)
	back = defaultdict(lambda:-1)
	for u,v in edges:
		adjlist[u].append(v)

	for u in path:
		for v in adjlist[u]:
			if result[u]+1 > result[v]:
				result[v] = result[u]+1
				#print(u,v,result[u],result[v])
				back[v] = u
				if result[v]>max_num[0]:
					max_num = result[v],v

	

	return max_num[0],solutions(back,max_num[1]) + [max_num[1]]


def solutions(back,num):

	if back[num]==-1:
		return []
	return solutions(back,back[num]) + [back[num]]

if __name__ == "__main__":

	print(longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))

	print(longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))

	print(longest(8, [(0,1), (0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7), (6,7)]))