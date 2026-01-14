#1, 2, 3 더하기
from sys import stdin
input = stdin.readline

T = int(input())

def solve(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    elif N == 3:
        return 4
    if N > 3:
        return solve(N-1) + solve(N-2) + solve(N-3)
    
for _ in range(T):
    tmp = int(input())
    print(solve(tmp))
