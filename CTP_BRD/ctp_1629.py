#곱셈
#DP로는 풀수 없는지?
from sys import stdin
input = stdin.readline

A, B, C = map(int, input().split())


def solve(N):
    if N == 1:
        return A%C
    if N == 2:
        return ((A**2)%C)
    elif N % 2 != 0:
        return (((solve(N//2)**2)*A)%C)
    else:
        return ((solve(N//2)**2)%C)
    

print(solve(B))