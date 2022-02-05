from collections import deque
class BFSResult:
	def __init__(self):
		self.level = {}
		self.parent = {}
class Graph:
	def __init__(self):
		self.adj = {}
	def add_edge(self, u, v):
		if self.adj[u] is None:
			self.adj[u] = []
		self.adj[u].append(v)


def bfs(g, s):
	r = BFSResult()
	r.parent = {s: None}
	r.level = {s: 0}	
	queue = deque()
	queue.append(s)
	while queue:
		u = queue.popleft()
		for n in g.adj[u]:
			if n not in level:
				r.parent[n] = u
				r.level[n] = r.level[u] + 1
				queue.append(n)
	return r
graph = Graph()
graph.add_edge('a','x')