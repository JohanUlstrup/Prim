import heapq
import time
"""
shoud have a run time of O(E*log(E))
E = edges 

eger primO(E*log(V))
"""

class Edge:
    def __init__(self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

def add_edges(node_index, matrix, visited, pq):
    visited[node_index] = True
    for end in range(len(matrix)):
        if matrix[node_index][end] > 0 and not visited[end]:
            heapq.heappush(pq, Edge(node_index, end, matrix[node_index][end]))

def lazy_prim(s, matrix):
    n = len(matrix)
    pq = []
    visited = [False] * n
    mst_edges = []
    mst_cost = 0
    edge_count = 0

    add_edges(s, matrix, visited, pq)

    while pq and edge_count < n - 1:
        edge = heapq.heappop(pq)
        node_index = edge.end

        if visited[node_index]:
            continue

        mst_edges.append(edge)
        mst_cost += edge.cost
        edge_count += 1
        add_edges(node_index, matrix, visited, pq)

    if edge_count != n - 1:
        return None, None

    return mst_cost, mst_edges

