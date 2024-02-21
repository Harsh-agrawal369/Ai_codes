from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = []

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        queue = []
        queue.append(s)
        self.visited.append(s)

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if i not in self.visited:
                    queue.append(i)
                    self.visited.append(i)

g = Graph()
n = int(input("Enter the number of edges you want to add: "))
for _ in range(n):
    u = input("Enter the source node: ")
    v = input("Enter the destination node: ")
    g.addEdge(u, v)

start_node = input("Enter the starting node for BFS: ")
g.BFS(start_node)
