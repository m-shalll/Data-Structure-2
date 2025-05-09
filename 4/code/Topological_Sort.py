from collections import deque
def topological_sort(graph):
    sortedElements=[]
    in_degree = {u: 0 for u in graph} # creates a dictionary which initializes each u with 0, to start counting incoming edges.
    for u in graph: # loops over each vertex in the graph.
        for v in graph[u]:
            in_degree[v] += 1
    n = deque()  # n is a queue of elements with no incoming edges.
    for u in graph:
        if in_degree[u] == 0:
            n.append(u)
    while(n):
        element = n.popleft()
        sortedElements.append(element)
        for neighbor in graph[element]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                n.append(neighbor)
    if len(sortedElements) != len(graph):
        print("ERROR: graph has at least 1 cycle!")
        return
    print(sortedElements)

graph = {
    1: [3],
    2: [1],
    3: [2]
}
topological_sort(graph)
