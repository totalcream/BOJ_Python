#연결 요소의 개수
from sys import stdin
input = stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = [[]] * (N+1)
visited = [False] * (N+1)

for i in range(M):
    F, T = map(int, input().split())
    if graph[F] == []:
        graph[F] = [T]
    else:
        graph[F].append(T)
    if graph[T] == []:
        graph[T] = [F]
    else:
        graph[T].append(F)

def BFS(graph, start, visited):

    dq = deque([start])
    visited[start] = True

    while dq:
        v = dq.popleft()
        for i in graph[v]:
            if not visited[i]:
                dq.append(i)
                visited[i] = True

#방문체크표(visited) 리스트를 순회하면서
#체크되지 않은 곳으로 다시 BFS로 탐색 후 cnt++
def check(graph, visited):
    cnt = 0
    for i in range(1, N+1):
        if visited[i]:
            continue

        BFS(graph, i, visited)
        cnt += 1

    return cnt

print(check(graph, visited))