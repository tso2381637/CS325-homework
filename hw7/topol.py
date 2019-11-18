from collections import defaultdict


def _order(n, edges):


	adjlist = defaultdict(list)
	indgree = defaultdict(int)

	for u,v in edges:
		adjlist[u].append(v)
		indgree[v] += 1


	head = 0
	queue = []
	for u in range(n):
		if indgree[u] == 0:
			queue.append(u)
	while(head<len(queue)):
		u = queue[head]
		yield u
		head+=1
		for v in adjlist[u]:
			indgree[v] -= 1
			if indgree[v] == 0:
				queue.append(v)

order = lambda n, edges: list(_order(n,edges))

if __name__ == "__main__":

	print(order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))