# code by Nguyen Tien Anh
# AI engineer & backend Developer
from numpy import Inf

nodes = {
    'F': 5,
    'E': 4,
    'B': 1,
    'C': 2,
    'D': 3,
    'A': 0
}
graph = {
    nodes['E']: [(5, 9), (3, 2)],
    nodes['B']: [(0, 7), (2, 1), (5, 11)],
    nodes['C']: [(1, 1), (3, 1)],
    nodes['D']: [(2, 1), (4, 5)],
    nodes['A']: [(5, 4), (1, 7)],
    nodes['F']: [(0, 4), (1, 11), (2, 20), (4, 9)]
}


def dijkstras(graph, root):
    n = len(graph)
    # Khởi tạo trọng số
    dist = [Inf for _ in range(n)]
    dist[root] = 0
    # danh sách những node đã xét
    visited = [False for _ in range(n)]
    # lặp qua các nodes
    for _ in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i
        if dist[u] == Inf:
            break
        visited[u] = True
        for v, l in graph[u]:
            if dist[u] + l < dist[v]:
                dist[v] = dist[u] + l
    return dist


print('Khoảng cách từ A đến E là: ', dijkstras(graph, nodes['C'])[nodes['F']])

# Tien Anh Nguyen