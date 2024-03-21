# 행렬 곱셈 순서

from sys import stdin
input = stdin.readline

N = int(input())
dp = [[0] * N for _ in range(N)]
lst = [list(map(int, input().split())) for _ in range(N)]

for term in range(1, N):
    for start in range(N):
        if start + term == N:
            break
        
        dp[start][start+term] = int(1e9)

        for t in range(start, start + term):
            dp[start][start + term] = min(dp[start][start + term], dp[start][t] + dp[t + 1][start + term] + lst[start][0] * lst[t][1] * lst[start + term][1])


print(dp[0][N - 1])