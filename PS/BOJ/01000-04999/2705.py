from sys import stdin
input = stdin.readline

t = int(input())

dp = [1,2,2,4,4]

for _ in range(t):
    n = int(input())
    if n <= len(dp):
        print(dp[n-1])
    else:
        for x in range(len(dp), n):
            if x//2:
                dp.append(dp[(x-1)//2] + dp[x-2])
            else:
                dp.append(dp[x-1]+2)
        print(dp[n-1])
