# 숨바꼭질 3
# 2024-05-14
# 다익스트라 or bfs or 등등

from sys import stdin
input = stdin.readline
from collections import deque


N, K = map(int, input().split())

dist = [0] * 100001
visited = [False] * 100001

queue = deque()
queue.append(N)
visited[N] = True

def dfs():
    while queue:
        x = queue.popleft()
        if x == K:
            return
        
        if 0 <= 2 * x < 100001 and not visited[2*x]:
            t = 2 * x
            dist[t] = dist[x]
            visited[t] = True
            queue.append(t)
        if 0 <= x - 1 < 100001 and not visited[x - 1]:
            t = x - 1
            dist[t] = dist[x] + 1
            visited[t] = True
            queue.append(t)
        if 0 <= x + 1 < 100001 and not visited[x + 1]:
            t = x + 1
            dist[t] = dist[x] + 1
            visited[t] = True
            queue.append(t)

dfs()
print(dist[K])