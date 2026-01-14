#계단 오르기
from sys import stdin
input = stdin.readline

N = int(input())

steps = [int(input()) for _ in range(N)]

dp = [0]*N

if N <= 2:
    print(sum(steps))
else:
    dp[0] = steps[0]
    dp[1] = steps[0] + steps[1]
    for i in range(2, N):
        dp[i] = max(dp[i-3] + steps[i-1] + steps[i], dp[i-2] + steps[i])
    print(dp[-1])