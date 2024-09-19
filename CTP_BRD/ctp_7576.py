#토마토
from sys import stdin
input = stdin.readline
from collections import deque

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

#(y, x) 순서
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

#토마토 위치 찾기
#익은 토마토 == 1, 익지 않은 토마토 == 0, 토마토가 없는 경우 == -1
tomato = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            tomato.append([i, j])

#토마토 익히기
while tomato:
    y, x = tomato.popleft()
    
    #4방향으로 뻗치기
    for dy, dx in dir:
        nx = x + dx
        ny = y + dy

        #올바른 범위인지 확인
        if 0 <= nx < M and 0 <= ny < N and board[ny][nx] == 0:
            tomato.append([ny, nx])
            #현재 상자에 1씩 더해서 day 계산
            board[ny][nx] = board[y][x] + 1

day = 0
for i in board:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    day = max(day, max(i))

print(day - 1)