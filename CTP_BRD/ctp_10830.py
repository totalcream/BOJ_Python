#행렬 제곱
from sys import stdin
input = stdin.readline

N, B = map(int, input().split())

arr = []
for i in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

lst = [[0] * N for _ in range(N)]

def dotmat(A, B):
    tmp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                tmp[i][j] += A[i][k] * B[k][j]
            tmp[i][j] %= 1000

    return tmp

dot1 = arr.copy()
dot2 = dotmat(arr, arr)

def solve(cnt):
    if cnt == 1:
        for i in range(N):
            for j in range(N):
                dot1[i][j] %= 1000
        return dot1
    if cnt == 2:
        return dot2
    tmp = solve(cnt//2)
    if cnt % 2 != 0:
        return dotmat(dotmat(tmp, tmp), dot1)
    else:
        return dotmat(tmp, tmp)

res = solve(B)

for i in res:
    print(*i)