# 파도반 수열
# 2024-05-08
# dp문제

from sys import stdin
input = stdin.readline

T = int(input())

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
for i in range(T):
    k = int(input())
    for j in range(6, k+1):
        dp[j] = dp[j - 5] + dp[j - 1]
    print(dp[k])