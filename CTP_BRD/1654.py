# 랜선 자르기

from sys import stdin
input = stdin.readline

N, K = map(int, input().split())

Cables = []
for i in range(N):
    Cables.append(int(input()))
start, end = 1, max(Cables)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in Cables:
        lines += i // mid
    
    if lines >= K:
        start = mid + 1
    else:
        end = mid - 1

print(end)