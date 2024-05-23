# RGB거리 2
# 2024-05-16
# DP, RGB거리의 변형문제
# 첫 집이 R, G, B일 때를 계산해봐야한다

from sys import stdin
input = stdin.readline

N = int(input())
seq = []
for i in range(N):
    seq.append(list(map(int, input().split())))

ans = E = 1e9
for j in range(3):
    dp = [[E, E, E] for _ in range(N)]
    dp[0][j] = seq[0][j]
    for i in range(1, N):
        dp[i][0] = seq[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = seq[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = seq[i][2] + min(dp[i-1][0], dp[i-1][1])
    for c in range(3):
        if j != c:
            ans = min(ans, dp[-1][c])

print(ans)