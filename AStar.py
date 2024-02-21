from queue import PriorityQueue

class Node:
    def __init__(self, name):
        self.name = name
        self.adjacencies = []  # List of tuples (neighbor, cost)
        self.g = float('inf')  # Cost from start to this node
        self.h = 0  # Heuristic from this node to goal
        self.f = float('inf')  # Total cost (g + h)
        self.parent = None  # For path reconstruction

    def add_edge(self, neighbor, cost=1):
        self.adjacencies.append((neighbor, cost))

def a_star_search(start, goal):
    open_set = PriorityQueue()
    start.g = 0
    start.f = start.h
    open_set.put((start.f, id(start), start))  # Use id(node) as a tiebreaker
    closed_set = set()

    while not open_set.empty():
        current = open_set.get()[2]  # Get the node

        if current == goal:
            return reconstruct_path(goal)

        closed_set.add(current)

        for neighbor, cost in current.adjacencies:
            if neighbor in closed_set:
                continue

            tentative_g = current.g + cost

            if tentative_g < neighbor.g:
                neighbor.parent = current
                neighbor.g = tentative_g
                neighbor.f = neighbor.g + neighbor.h
                if not any(neighbor == item[2] for item in open_set.queue):
                    open_set.put((neighbor.f, id(neighbor), neighbor))

    return []

def reconstruct_path(current_node):
    path = []
    total_cost = current_node.g  # The total cost is the g value of the goal node
    while current_node:
        path.append(current_node.name)
        current_node = current_node.parent
    return path[::-1], total_cost

if __name__ == "__main__":
    nodes = {}

    # Input for nodes and heuristics
    num_nodes = int(input("Enter number of nodes: "))
    for _ in range(num_nodes):
        name = input("Enter node name: ")
        heuristic = int(input(f"Enter heuristic value for {name}: "))
        nodes[name] = Node(name)
        nodes[name].h = heuristic

    # Input for edges
    num_edges = int(input("Enter number of edges: "))
    for _ in range(num_edges):
        start, end, cost = input("Enter edge (start end cost): ").split()
        cost = int(cost)
        nodes[start].add_edge(nodes[end], cost)

    # Start and goal
    start_node = input("Enter start node: ")
    goal_node = input("Enter goal node: ")

    path, total_cost = a_star_search(nodes[start_node], nodes[goal_node])

    if path:
        print("Path found:", " -> ".join(path))
        print(f"Total cost: {total_cost}")
    else:
        print("No path found.")
