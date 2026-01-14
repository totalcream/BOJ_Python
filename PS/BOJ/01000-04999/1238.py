# 파티
from sys import stdin
import heapq
input = stdin.readline

INF = 1e10
N, M, X = map(int, input().split())

#graph = {i: {} for i in range(N)}
graph = [[] for _ in range(N+1)]
reverse_graph = [[] for _ in range(N+1)]

for i in range(M):
    start_line, end_line, value = map(int, input().split())
    graph[start_line].append((end_line, value))
    reverse_graph[end_line].append((start_line,value))

def dijkstra_list(graph, start, mode = 1):
    dist = [INF] * (N+1)
    q = []
    heapq.heappush(q,(start,0))
    while q:
        w,d = heapq.heappop(q)
        if dist[w] < d:
            continue
        for nxt,c in graph[w]:
            if dist[nxt] > d + c:
                dist[nxt] = d+c
                heapq.heappush(q,(nxt,d+c))
    return dist

# def dijkstra_dict(graph, start):
#     distances = {node: float('inf') for node in graph}
#     distances[start] = 0
#     queue = []
#     heapq.heappush(queue, [distances[start], start])

#     while queue:
#         current_distance, current_destination = heapq.heappop(queue)

#         if distances[current_destination] < current_distance:
#             continue

#         for new_destination, new_distance in graph[current_destination].item():
#             distance = current_distance + new_distance
#             if distance < distances[new_destination]:
#                 distances[new_destination] = distance
#                 heapq.heappush(queue, [distance, new_destination])
    
#     return distances

node2x = dijkstra_list(reverse_graph, X)
x2node = dijkstra_list(graph, X)

print(max([x2node[i] + node2x[i] for i in range(1,N+1) if i != X]))