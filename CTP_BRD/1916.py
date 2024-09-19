# 최소비용 구하기
# 2025-05-17
# 다익스트라

from sys import stdin
import heapq
input = stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())

def dijkstra(graph, start):
    # 거리를 무한대로 초기화
    distances = [float('inf')] * (len(graph))
    # 시작 노드의 거리를 0으로 설정
    distances[start] = 0
    # 우선순위 큐를 생성하여 노드와 거리를 저장
    queue = [(0, start)]
    while queue:
        # 큐에서 거리가 가장 작은 노드를 가져옴
        current_distance, current_node = heapq.heappop(queue)
        # 현재 거리가 저장된 거리보다 크면 건너뜀
        if current_distance > distances[current_node]:
            continue
        # 현재 노드의 이웃 노드들을 순회
        for neighbor, weight in graph[current_node]:
            # 이웃 노드까지의 새로운 거리 계산
            distance = current_distance + weight
            # 새로운 거리가 저장된 거리보다 작으면 업데이트
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # 새로운 거리로 이웃 노드를 큐에 추가
                heapq.heappush(queue, (distance, neighbor))
    return distances
# 그래프와 시작 노드를 인자로하여 다익스트라 함수 호출
distances = dijkstra(graph, start)
# 도착 노드까지의 거리 출력
print(distances[end])