from sys import stdin, maxsize

C, N = map(int, input().split())
cost = [list(map(int, input().split())) for _ in range(N)]

dp = [0] + [maxsize] * (C + 101)

for i, j in cost:
    for cc in range(j, C + 101):
        dp[cc] = min(dp[cc], dp[cc - j] + i)

print(min(dp[C:C + 101]))