# 최솟값 찾기
# 2024-09-19

from sys import stdin
from collections import deque
input = stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))

slwindow = deque()

for i in range(N):
    while slwindow and slwindow[-1][1] > A[i]:
        slwindow.pop()
    
    slwindow.append((i + 1, A[i]))

    if slwindow[-1][0] - slwindow[0][0] >= L:
        slwindow.popleft()
    
    print(slwindow[0][1], end=' ')

