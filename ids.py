# Iterative Deepening Search

from collections import defaultdict

class Graph:
	def __init__(self,vertices):
		self.V = vertices
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def DLS(self,src,target,maxDepth):

		if src == target : return True

		if maxDepth <= 0 : return False
		for i in self.graph[src]:
				if(self.DLS(i,target,maxDepth-1)):
					return True
		return False

	def IDDFS(self,src, target, maxDepth):
		for i in range(maxDepth):
			if (self.DLS(src, target, i)):
				return True
		return False

if __name__ == "__main__":
    vertices = int(input("Enter the number of vertices: "))
    g = Graph(vertices)

    while True:
        u = (input("Enter source vertex (or -1 to stop): "))
        if u == '-1':
            break
        v = (input("Enter destination vertex: "))
        g.addEdge(u, v)

    target = (input("Enter the target vertex: "))
    maxDepth = int(input("Enter the maximum depth: "))
    src = (input("Enter the source vertex: "))

    if g.IDDFS(src, target, maxDepth):
        print("Target is reachable from source within max depth.")
    else:
        print("Target is NOT reachable from source within max depth.")
