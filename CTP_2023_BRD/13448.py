# SW 역량 테스트
# 2024-06-12
# DP, 그리디

from sys import stdin
input = stdin.readline

N, T = map(int, input().split())
M = list(map(int, input().split()))
P = list(map(int, input().split()))
R = list(map(int, input().split()))

contests = [(M[i], P[i], R[i]) for i in range(N)]
contests.sort(key=lambda x: x[2] / x[1])

dp = [0] * (T + 1)

for i in contests:
    for j in range(T, i[2] - 1, -1):
        dp[j] = max(dp[j], dp[j - i[2]] + i[0] - j * i[1])

print(max(dp))