# 편세권
# 2024-05-20
# bfs로 접근해야하는데 모든 집에 대해서 bfs를 돌리면 시간초과가 난다.
# 


from sys import stdin
input = stdin.readline
from collections import deque

N, M, R, C = map(int, input().split())

jido = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

homes = []
for i in range(R):
    a, b, p = map(int, input().split())
    jido[a-1][b-1] = 1
    homes.append((a-1, b-1, p))

combi = []
for i in range(C):
    cx, cy = map(int, input().split())
    jido[cx-1][cy-1] = 2

dq = deque()

def bfs(ax, ay):
    dq.append((ax, ay))
    visited[ax][ay] = True
    while dq:
        x, y = dq.popleft()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if jido[nx][ny] == 2:
                    return abs(ax - nx) + abs(ay - ny)
                dq.append((nx, ny))

ans = 1e9
for x, y, p in homes:
    visited = [[False] * M for _ in range(N)]
    ans = min(ans, (bfs(x, y) * p))
print(ans)