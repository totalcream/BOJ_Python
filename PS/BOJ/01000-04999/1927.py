#최소 힙
from sys import stdin
input = stdin.readline
from heapq import *

N = int(input())

lst = []
que = []

for _ in range(N):
    lst.append(int(input()))

for i in lst:
    if i == 0 and len(que) != 0:
        print(heappop(que))
    elif i == 0 and len(que) == 0:
        print('0')
    elif i:
        heappush(que, i)

        