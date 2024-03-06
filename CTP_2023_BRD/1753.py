# 최단경로
# Heap으로 구현
from sys import stdin
import heapq
input = stdin.readline

INF = 1e8

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

print(graph)
def dijkstra_list(graph, start):
    distances = [INF] * (V+1)
    queue = []
    heapq.heappush(queue, (0, start)) # 우선순위, 값 형태
    distances[start] = 0

    while queue:
        distance, now = heapq.heappop(queue) #우선순위가 가장 낮은 값이 나옴(거리 낮은 순)

        if distances[now] < distance: # 이미 입력되어 있는 값이 현재노드까지보다 거리가 작다면 이미 방문한 노드
            continue

        for i in graph[now]: # 연결된 모든 노드 탐색
            cur_cost = distances[now] + i[1]
            if cur_cost < distances[i[0]]: # 기존에 입력되어있는 값보다 크다면
                distances[i[0]] = cur_cost
                heapq.heappush(queue, (cur_cost, i[0]))

    return distances

ans = dijkstra_list(graph, K)

for i in ans:
    if i == INF:
        print("INF")
    else:
        print(i)


