#피보나치 수
from sys import setrecursionlimit
from functools import cache

N = int(input())
setrecursionlimit(100000)
@cache
def solve(N):
    if N == 1 or N == 2:
        return 1
    else:
        return solve(N - 1) + solve(N - 2)
    
print(solve(N))