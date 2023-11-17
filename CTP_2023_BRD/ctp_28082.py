#기계오리 연구
from sys import stdin
input = stdin.readline
import math

N, K = map(int, input().split())
case = list(map(int, input().split()))
case.sort()

dp = [math.inf] * 50001
dp[0] = 0

for i in case:
    for j in range(50000, 0, -1):
        if (dp[j] > 0) and (dp[j] < K):
            dp[j + i] = min(dp[j + i], dp[j] + 1)
    dp[i] = 1

ans = []
for idx, i in enumerate(dp):
    if i != 0 and i != math.inf:
        ans.append(idx)

print(len(ans))
print(*ans)