# 미로 탐색
# 2024-05-15
# BFS 어디선가 풀어본 듯한 느낌

from sys import stdin, setrecursionlimit
input = stdin.readline
from collections import deque

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip())))

visited = [[0 for _ in range(M)] for _ in range(N)]
dist = [[-1 for _ in range(M)] for _ in range(N)]
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
dq = deque()
def bfs():
    while dq:
        y, x = dq.popleft()

        for dy, dx in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and board[ny][nx] == 1:
                visited[ny][nx] = 1
                dist[ny][nx] = dist[y][x] + 1
                dq.append((ny, nx))

visited[0][0] = 1
dist[0][0] = 0
dq.append((0, 0))
bfs()

print(dist[N - 1][M - 1]+1)