class Node:
    def __init__(self, name, heuristic=0):
        self.name = name
        self.heuristic = heuristic  # Estimated cost to goal
        self.adjacencies = []  # List of tuples (neighbor, cost)
        self.parent = None  # Track the path

    def add_edge(self, neighbor, cost=1):
        self.adjacencies.append((neighbor, cost))


def greedy_best_first_search(start, goal):
    from queue import PriorityQueue

    frontier = PriorityQueue()
    frontier.put((start.heuristic, start))
    visited = set()

    while not frontier.empty():
        current = frontier.get()[1]  # Get node from priority queue

        if current == goal:
            return reconstruct_path(goal)

        visited.add(current.name)

        for neighbor, _ in current.adjacencies:
            if neighbor.name not in visited and neighbor.parent is None:
                neighbor.parent = current
                frontier.put((neighbor.heuristic, neighbor))
    return None

def reconstruct_path(goal):
    path = []
    current = goal
    while current:
        path.append(current.name)
        current = current.parent
    path.reverse()
    return path


if __name__ == "__main__":
    # Create nodes and heuristics
    nodes = {}
    node_names = input("Enter node names and heuristics (e.g., A,1 B,2): ").split()
    for nh in node_names:
        name, heuristic = nh.split(',')
        nodes[name] = Node(name, int(heuristic))

    # Add edges
    while True:
        edge = input("Enter edge and cost (e.g., A B 1) or type 'done': ")
        if edge.lower() == 'done':
            break
        start, end, cost = edge.split()
        nodes[start].add_edge(nodes[end], int(cost))

    # Perform search
    start_node = input("Enter start node: ")
    goal_node = input("Enter goal node: ")
    path = greedy_best_first_search(nodes[start_node], nodes[goal_node])

    if path:
        print("Path found:", " -> ".join(path))
    else:
        print("No path found.")
