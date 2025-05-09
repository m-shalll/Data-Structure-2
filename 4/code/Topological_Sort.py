def TopologicalSort(graph):
    sortedElements=[]
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    n = set()  # n is a set of elements with no incoming edges
    for u in graph:
        if in_degree[u] == 0:
            n.add(u)
    while(n):
        element = n.pop()
        sortedElements.append(element)
        for neighbor in graph[element]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                n.add(neighbor)
    if len(sortedElements) != len(graph):
        print("ERROR: graph has at least 1 cycle!")
        return
    print(sortedElements)

graph = {
    1: [2],
    2: [3],
    3: [1]
}
TopologicalSort(graph)
