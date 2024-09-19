#피보나치 수 3
N = int(input())
dp = [0] * (1500000)
dp[1] = 1

for i in range(2, 1500000):
    dp[i] = dp[i-1] + dp[i-2]
    dp[i] %= 1000000

print(dp[N%1500000])