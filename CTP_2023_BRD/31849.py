# 편세권
# 2024-05-20
# bfs로 접근해야하는데 모든 집에 대해서 bfs를 돌리면 시간초과가 난다.
# multi-source bfs를 이용하여 모든 편의점에서 동시에 bfs를 수행한다.
# 그리고 각 집에 대해 편의점까지의 최소 거리를 이용해 점수를 계산하고 최소 점수를 찾는다.

# from sys import stdin
# input = stdin.readline
# from collections import deque

# N, M, R, C = map(int, input().split())

# jido = [[0] * M for _ in range(N)]
# visited = [[False] * M for _ in range(N)]

# homes = []
# for i in range(R):
#     a, b, p = map(int, input().split())
#     jido[a-1][b-1] = 1
#     homes.append((a-1, b-1, p))

# combi = []
# for i in range(C):
#     cx, cy = map(int, input().split())
#     jido[cx-1][cy-1] = 2

# dq = deque()

# def bfs(ax, ay):
#     dq.append((ax, ay))
#     visited[ax][ay] = True
#     while dq:
#         x, y = dq.popleft()
#         for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
#                 visited[nx][ny] = 1
#                 if jido[nx][ny] == 2:
#                     return abs(ax - nx) + abs(ay - ny)
#                 dq.append((nx, ny))

from sys import stdin
from collections import deque

input = stdin.readline

N, M, R, C = map(int, input().split())

homes = []
stores = []

# 각 집의 위치와 월세를 입력 받음
for _ in range(R):
    a, b, p = map(int, input().split())
    homes.append((a-1, b-1, p))

# 각 편의점의 위치를 입력 받음
for _ in range(C):
    cx, cy = map(int, input().split())
    stores.append((cx-1, cy-1))

# 모든 편의점에서 동시에 BFS 수행
def multi_source_bfs(stores, N, M):
    distances = [[float('inf')] * M for _ in range(N)]
    dq = deque()
    for cx, cy in stores:
        dq.append((cx, cy))
        distances[cx][cy] = 0

    while dq:
        x, y = dq.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and distances[nx][ny] == float('inf'):
                distances[nx][ny] = distances[x][y] + 1
                dq.append((nx, ny))
    
    return distances

distances = multi_source_bfs(stores, N, M)

min_score = float('inf')

# 각 집에 대해 편의점까지의 최소 거리를 이용해 점수를 계산하고 최소 점수를 찾음
for x, y, p in homes:
    score = distances[x][y] * p
    if score < min_score:
        min_score = score

print(min_score)