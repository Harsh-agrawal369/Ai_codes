# import numpy as np
# import heapq

# class Node:
#     def __init__(self, state, parent=None):
#         self.state = state
#         self.parent = parent
#         self.g = 0
#         self.h = 0

#     def __eq__(self, other):
#         return self.state == other.state

#     def __lt__(self, other):
#         return (self.g + self.h) < (other.g + other.h)

# def heuristic(state, problem):
#     return np.min(problem[state, :])

# def a_star_search(problem):
#     start_state = 0
#     frontier = []
#     heapq.heappush(frontier, Node(start_state))

#     explored = set()

#     while frontier:
#         node = heapq.heappop(frontier)
#         state = node.state

#         if len(explored) == problem.shape[0]:
#             path = []
#             total_cost = 0
#             while node.parent:
#                 path.append(node.state)
#                 total_cost += problem[node.parent.state, node.state]
#                 node = node.parent
#             path.append(start_state)
#             total_cost += problem[node.state, start_state]
#             path.reverse()
#             return path, total_cost

#         explored.add(state)

#         for next_state in range(problem.shape[0]):
#             if next_state not in explored:
#                 child = Node(next_state, node)
#                 child.g = node.g + problem[state, next_state]
#                 child.h = heuristic(next_state, problem)
#                 heapq.heappush(frontier, child)


# # Initialize an empty cost matrix
# cost_matrix = []


# # Solve the problem using A* search
# inp = int(input("Enter th enumber of cities: "))
# for i in range(0,inp):
#     arr = list(map(int, input("Enter the cost of reaching each city in series separated by space: ").split()))
#     cost_matrix.append(arr)

# # Solve the problem using A* search
# optimal_path, total_cost = a_star_search(np.array(cost_matrix))


# print("Optimal Path:", optimal_path)
# print("Total Cost of Travelling:", total_cost)

import numpy as np
def travellingsalesman(c):
    global cost
    adj_vertex = 999
    min_val = 999
    visited[c] = 1
    print((c + 1), end=" ")
    for k in range(n):
        if (tsp_g[c][k] != 0) and (visited[k] == 0):
            if tsp_g[c][k] < min_val:
                min_val = tsp_g[c][k]
                adj_vertex = k
    if min_val != 999:
        cost = cost + min_val
    if adj_vertex == 999:
        adj_vertex = 0
        print((adj_vertex + 1), end=" ")
        cost = cost + tsp_g[c][adj_vertex]
        return
    travellingsalesman(adj_vertex)
n = 5
cost = 0
visited = np.zeros(n, dtype=int)
tsp_g = []
inp = int(input("Enter th enumber of cities: "))
for i in range(0,inp):
    arr = list(map(int, input("Enter the cost of reaching each city in series separated by space: ").split()))
    tsp_g.append(arr)
tsp_g = np.array(tsp_g)

print("Shortest Path:", end=" ")
travellingsalesman(0)
print()
print("Minimum Cost:", end=" ")
print(cost)
