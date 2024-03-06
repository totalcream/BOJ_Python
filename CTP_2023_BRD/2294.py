# 동전2

from sys import stdin
input = stdin.readline

N, K = map(int, input().split())

coins = []

for i in range(N):
    coins.append(int(input().rstrip()))

dp = [10001] * (K+1)
dp[0] = 0

for coin in coins:
    for i in range(coin, K+1):
        dp[i] = min(dp[i], dp[i-coin] + 1)

if dp[K] == 10001:
    print(-1)
else:
    print(dp[K])
