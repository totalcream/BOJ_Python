#쿼드트리
from sys import stdin
input = stdin.readline

N = int(input())

arr = [list(map(int, list(input().strip()))) for _ in range(N)]

def check(X, Y, N):
    for i in range(Y, Y+N):
        for j in range(X, X+N):
            if arr[Y][X] != arr[i][j]:
                print("(", end="")
                check(X, Y, N // 2)
                check(X + N // 2, Y, N // 2) #X먼저
                check(X, Y + N // 2, N // 2)
                check(X + N // 2, Y + N // 2, N // 2)
                print(")", end="")
                return
    if arr[Y][X] == 1:
        print(1, end="")
    else:
        print("0", end="")

check(0, 0, N)