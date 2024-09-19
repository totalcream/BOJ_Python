#체스판 다시 칠하기
from sys import stdin
input = stdin.readline


N, M = map(int, input().split())
board = []
cnt = []

for i in range(N):
    board.append(input())

for i in range(N-7):
    for j in range(M-7): #
        W_idx = 0
        B_idx = 0
        for y in range(i, i+8):
            for x in range(j, j+8):
                if (y + x) % 2 == 0:
                    if board[y][x] != 'W':
                        W_idx += 1
                    else:
                        B_idx += 1
                else:
                    if board[y][x] != 'W':
                        B_idx += 1
                    else:
                        W_idx += 1
        
        cnt.append(W_idx)
        cnt.append(B_idx)
print(min(cnt))