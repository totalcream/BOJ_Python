#토마토
from sys import stdin
input = stdin.readline
from collections import deque

M, N, H = map(int, input().split())

#상 하 좌 우 위 아래
#z y x순
dir = [(-1, 0, 0), (1, 0, 0),
       (0, 1, 0), (0, -1, 0),
       (0, 0, 1), (0, 0, -1)]

#토마토 0 == 덜익음, 1 == 익음, -1 == 없음
board = []
for _ in range(H):
    tmp = [list(map(int, input().split())) for _ in range(N)]
    board.append(tmp)        

tomato = deque()
for i in range(H):
    for j in range(N):
            for k in range(M):
                if board[i][j][k] == 1:
                    tomato.append([i, j, k])

while tomato:
     z, y, x = tomato.popleft()
     for dz, dy, dx in dir:
          nx = x + dx
          ny = y + dy
          nz = z + dz
          if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and board[nz][ny][nx] == 0:
               tomato.append([nz, ny, nx])
               #1씩 더해서 max값을 찾으면 다 뻗은 날의 값
               board[nz][ny][nx] = board[z][y][x] + 1

day = 0
for i in board:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        day = max(day, max(j))

print(day - 1)
