# 1, 2, 3 더하기 3
# 2024-05-08
# dp문제

from sys import stdin
input = stdin.readline


T = int(input())
dp = [0] * 1000001
mod = 1000000009
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(T):
    k = int(input())
    for j in range(4, k+1):
        dp[j] = (dp[j-1] + dp[j - 2] + dp[j - 3]) % mod
    print(dp[k])