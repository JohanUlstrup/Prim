import heapq
import time
import numpy as np
import matplotlib.pyplot as plt
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

def measure_time(matrix_size):
    times = []
    for _ in range(10):  # Run 3 tests for each matrix size
        matrix = np.random.randint(0, 10, (matrix_size, matrix_size))  # Random cost matrix
        np.fill_diagonal(matrix, 0)  # No self-loops (diagonal 0)
        start_time = time.time()
        lazy_prim(0, matrix)
        times.append(time.time() - start_time)
    return np.mean(times)  # Return average time

# # Test and plot
# matrix_sizes = range(10, 101, 10)  # Test with sizes from 10 to 100
# avg_times = []

# for size in matrix_sizes:
#     avg_elapsed_time = measure_time(size)
#     avg_times.append(avg_elapsed_time)

# # Plotting the results
# plt.plot(matrix_sizes, avg_times, marker='o')
# plt.xlabel('Matrix Size (n)')
# plt.ylabel('Average Time (seconds)')
# plt.title('Average Performance of Lazy Prim Algorithm')
# plt.grid(True)
# plt.show()
# Test and plot


matrix_sizes = range(10, 1001, 10)  # Test with sizes from 10 to 100
avg_times = []
log_times = []
sizes = []

for size in matrix_sizes:
    avg_elapsed_time = measure_time(size)
    avg_times.append(avg_elapsed_time)
    log_times.append(avg_elapsed_time / (size * np.log(size)))
    sizes.append(size)

# Output the results
print(f"Matrix Sizes: {sizes}")
print(f"Average Times: {avg_times}")


# Plotting the results
plt.plot(matrix_sizes, avg_times, marker='o')
plt.xlabel('Matrix Size (n)')
plt.ylabel('Log(Normalized Time) (seconds)')
plt.title('Log-Normalized Performance of Lazy Prim Algorithm')
plt.grid(True)
plt.show()