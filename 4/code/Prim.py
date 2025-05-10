import heapq

def prim_mst(graph, start=0):
    n = len(graph)
    in_tree = [False] * n         # Track if vertex is in MST
    D = [float('inf')] * n        
    parent = [None] * n           # Store parent for MST
    D[start] = 0                  
    pq = [(0, start)]             # Priority queue with (distance, vertex)
    mst = []

    while pq:
        d_u, u = heapq.heappop(pq)
        if in_tree[u]:
            continue
        in_tree[u] = True

        if parent[u] is not None:
            mst.append((parent[u], u, d_u))

        for v, weight in graph[u]:
            if not in_tree[v] and weight < D[v]:
                D[v] = weight
                parent[v] = u
                heapq.heappush(pq, (D[v], v))

    return mst


graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)]
}


adj_list = [graph[i] for i in range(len(graph))]
mst = prim_mst(adj_list)

print("Edges in MST:")
for u, v, weight in mst:
    print(f"{u} - {v} with weight {weight}")
