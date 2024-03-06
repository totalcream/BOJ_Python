# 평범한 배낭

from sys import stdin
imput = stdin.readline

N, K = map(int, input().split())

lst = []

for i in range(N):
    W, V = map(int, input().split())
    lst.append((W, V))

dp = [0 for _ in range(K + 1)]
for item in lst:
    W, V = item
    for i in range(K, W-1, -1):
        dp[i] = max(dp[i], dp[i-W] + V)

print(dp[-1])