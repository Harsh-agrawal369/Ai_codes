def  uniform_cost_search(goal, start):

    global graph,cost
    answer = []

    queue = []

    for i in range(len(goal)):
        answer.append(10**8)

    queue.append([0, start])

    visited = {}

    count = 0

    while (len(queue) > 0):

        queue = sorted(queue)
        p = queue[-1]

        del queue[-1]

        p[0] *= -1

        if (p[1] in goal):

            index = goal.index(p[1])

            if (answer[index] == 10**8):
                count += 1

            if (answer[index] > p[0]):
                answer[index] = p[0]

            del queue[-1]
 
            queue = sorted(queue)
            if (count == len(goal)):
                return answer

        if (p[1] not in visited):
            for i in range(len(graph[p[1]])):

                queue.append( [(p[0] + cost[(p[1], graph[p[1]][i])])* -1, graph[p[1]][i]])

        visited[p[1]] = 1
 
    return answer


if __name__ == '__main__':

    graph,cost = [[] for i in range(10)],{}

    while True:
        u = int(input("Enter Node: "))
        if u == -1:
            break
        v = int(input("Enter destination: "))
        graph[u].append(v)
        c = int(input("Enter the cost: "))
        cost[(u, v)] = c

    goal = []

    print("Calculate cost between: ")
    a = int(input())
    b = int(input())
    goal.append(b)
 
    answer = uniform_cost_search(goal, a)

    print("Minimum cost = ",answer[0])