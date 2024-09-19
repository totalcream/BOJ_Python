# Triangulation
# 2024-05-08
# 

N = int(input())

dp = [0] * (1000001)
dp[3] = 0
dp[4] = 1
dp[5] = 2

for i in range(6, N+1):
    tmp = i % 2
    if tmp == 0:
        dp[i] = dp[i//2] + 2
    else:
        dp[i] = dp[i//2+1] +2

print(dp[N])