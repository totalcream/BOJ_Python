# K번째 최단경로 찾기
# 2024-06-06
# 다익스트라

import heapq
from collections import defaultdict

from sys import stdin
input = stdin.readline

def kth_shortest_path(n, m, k, edges):
    graph = defaultdict(list)
    for a, b, c in edges:
        graph[a].append((b, c))
    
    distances = [[float('inf')] * k for _ in range(n + 1)]
    distances[1][0] = 0
    
    pq = [(0, 1)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if distances[current_node][k-1] < current_distance:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor][k-1]:
                distances[neighbor][k-1] = distance
                distances[neighbor].sort()
                heapq.heappush(pq, (distance, neighbor))
    
    result = []
    for i in range(1, n + 1):
        if distances[i][k-1] == float('inf'):
            result.append(-1)
        else:
            result.append(distances[i][k-1])
    
    return result

N, M, K = map(int, input().split())
edges = []
index = 3
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
    index += 3

# 결과 계산 및 출력
result = kth_shortest_path(N, M, K, edges)
for res in result:
    print(res)