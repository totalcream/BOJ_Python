from sys import stdin
from collections import deque
input = stdin.readline

N, K = map(int, input().split())

dp = deque()
ysps_list = []
for i in range(N):
    dp.append(i+1)

while dp:
    for _ in range(K-1):
        dp.append(dp.popleft())
    
    ysps_list.append(dp.popleft())

print(str(ysps_list).replace('[', '<').replace(']', '>'))
