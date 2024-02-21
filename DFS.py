from collections import defaultdict

class Graph:
    def __init__ (self):
        self.graph = defaultdict(list)

    def addEdge(self, u , v):
        self.graph[u].append(v)

    def DFSUtil(self, u, visited):
        visited.add(u)
        print(u, end=' ')

        for neighbour in self.graph[u]:
            if neighbour not in visited:
                self.DFSUtil(neighbour,visited)
    
    def DFS(self, v):
        visited=set()
        self.DFSUtil(v,visited)

if __name__ == "__main__":
    g = Graph()
    print("Please enter the edge following by their edges seperated by space , 0 to exit: ")
    
    while(True):
        inp = input()
        if(inp=='0'):
            break
        li = list(inp.split(" "))
        
        for i in range(1,len(li)):
            g.addEdge(li[0], li[i])

    inp = input("Enter the root element: ") 

    g.DFS(inp)
