# 행복 유치원
# 2024-05-06
# 그리디 문제
# 

from sys import stdin
input = stdin.readline

N, K = map(int, input().split())

kids = list(map(int, input().split()))
diff = [] 
for i in range(0, N-1):
    diff.append(kids[i+1]-kids[i])

diff.sort()

ans = 0

for i in range(N-K):
    ans += diff[i]

print(ans)