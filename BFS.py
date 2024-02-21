from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        # Convert u to integer before appending to the graph
        self.graph[int(u)].append(int(v))

        
    def BFS(self, s):
 
        visited = [False] * (max(self.graph) + 1)
 
        queue = []
 
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            s = queue.pop(0)
            print(s, end=" ")
 
           
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

if __name__ == "__main__":
    g = Graph()
    print("Please enter the edge following by their edges separated by space: ")

    while True:
        inp = input()
        if inp == '0':
            break
        li = list(inp.split(" "))

        for i in range(1, len(li)):
            g.addEdge(int(li[0]), int(li[i]))

    inp = input("Enter the root element: ")

    g.BFS(int(inp))

