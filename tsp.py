from queue import PriorityQueue

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v, weight):
        self.adj_matrix[u][v] = weight
        self.adj_matrix[v][u] = weight

    def get_mst_cost(self):
        visited = [False] * self.num_vertices
        mst_cost = 0
        visited[0] = True
        priority_queue = PriorityQueue()

        for v in range(1, self.num_vertices):
            if self.adj_matrix[0][v] != 0:
                priority_queue.put((self.adj_matrix[0][v], v))

        while not priority_queue.empty():
            cost, u = priority_queue.get()
            if not visited[u]:
                visited[u] = True
                mst_cost += cost
                for v in range(self.num_vertices):
                    if not visited[v] and self.adj_matrix[u][v] != 0:
                        priority_queue.put((self.adj_matrix[u][v], v))

        return mst_cost

def tsp_a_star(graph):
    num_vertices = graph.num_vertices
    start_node = 0
    goal_node = start_node
    open_set = PriorityQueue()
    open_set.put((0, start_node, [start_node]))

    while not open_set.empty():
        f, current_node, path = open_set.get()

        if len(path) == num_vertices:
            if graph.adj_matrix[current_node][goal_node] != 0:
                path.append(goal_node)
                return path

        for next_node in range(num_vertices):
            if next_node not in path and graph.adj_matrix[current_node][next_node] != 0:
                new_path = path + [next_node]
                g = len(new_path) - 1
                h = graph.get_mst_cost()
                f = g + h
                open_set.put((f, next_node, new_path))

    return None

if __name__ == "__main__":
    num_vertices = int(input("Enter the number of vertices: "))
    graph = Graph(num_vertices)

    print("Enter the adjacency matrix (enter 0 if no edge exists): ")
    for i in range(num_vertices):
        for j in range(num_vertices):
            weight = int(input(f"Enter weight from vertex {i} to vertex {j}: "))
            graph.add_edge(i, j, weight)

    print("\nCalculating the shortest tour using A* search...")
    shortest_tour = tsp_a_star(graph)

    if shortest_tour:
        print("Shortest tour: ", shortest_tour)
    else:
        print("No tour found.")