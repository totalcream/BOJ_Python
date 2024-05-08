# 자전거 묘기
# 2024-05-08
# dp문제

from sys import stdin
input = stdin.readline

N = int(input())
seq = list(map(int, input().split()))

dp = [0] * 200001
for i in range(N-1, -1, -1):
    if i == N-1:
        dp[i] = 1
    else:
        if seq[i] == 0:
            dp[i] = dp[i+1] + 1
        else:
            if i + seq[i] + 1 >= N:
                dp[i] = 1
            else:
                dp[i] = dp[i + seq[i] + 1] + 1

for i in range(N):
    print(f"{dp[i]}", end=' ')