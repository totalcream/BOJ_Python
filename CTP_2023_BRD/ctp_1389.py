#케빈 베이컨의 6단계 법칙
from sys import stdin
input = stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False]* (N+1)

res = []

def BFS(i):
    visited = [0] * (N+1)
    queue.append(i)
    visited[i] = 1
    while queue:
        t = queue.popleft()
        for v in graph[t]:
            if not visited[v]:
                visited[v] = visited[t]+1
                queue.append(v)
    return sum(visited)

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

queue = deque()
res = []
for i in range(1, N+1):
    res.append(BFS(i))

print(res.index(min(res))+1)