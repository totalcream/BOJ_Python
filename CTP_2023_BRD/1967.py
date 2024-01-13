# 트리의 지름
from sys import stdin, setrecursionlimit
from collections import deque
input = stdin.readline

setrecursionlimit(10^4)

N = int(input())

graph = [[] for _ in range(N+1)]

for i in range(N-1):
    node_no, child, value = map(int, input().split())
    graph[node_no].append((child, value))
    graph[child].append((node_no, value))


def bfs(start, graph, mode):
    queue = deque()
    visited = [-1 for _ in range(N+1)]
    visited[start] = 0
    queue.append(start)

    while queue:
        node = queue.popleft()
        for child, value in graph[node]:
            if visited[child] == -1:
                visited[child] += (value + visited[node] + 1)
                queue.append(child)

    if mode == 1:
        # print(visited)
        return visited.index(max(visited))
    else:
        return max(visited)

idx = bfs(1, graph, 1)
print(bfs(idx, graph, 0))