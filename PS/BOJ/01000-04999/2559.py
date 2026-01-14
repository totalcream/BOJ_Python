# 수열

from sys import stdin
input = stdin.readline

N, K = map(int, input().split())

arr = list(map(int, input().split()))
S = sum(arr[:K])
ans = S

for i in range(N - K):
    S += arr[i+K] - arr[i]
    if ans < S:
        ans = S

print(ans)