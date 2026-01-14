# 구간 합 구하기 4

from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

arr = [0] + list(map(int, input().split()))
Sum = [0] * (N + 1)

for i in range(1, N + 1):
    Sum[i] = Sum[i - 1] + arr[i]

for _ in range(M):
    x, y = map(int, input().split())
    print(Sum[y] - Sum[x - 1])

