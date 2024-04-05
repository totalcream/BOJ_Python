# 공유기 설치

from sys import stdin
from bisect import bisect_left, bisect_right
input = stdin.readline

N, C = map(int, input().split())

lst = []
for _ in range(N):
    lst.append(int(input()))

lst.sort()

s, e = 1, max(lst) - min(lst)

while 1:
    mid = (s+e) // 2

    start = lst[0]
    start_idx = 0
    cnt = 0
    while start_idx < len(lst):
        cnt += 1
        start_idx = bisect_left(lst, lst[start_idx] + mid)

    if cnt < C:
        e = mid - 1
    elif cnt >= C:
        s = mid + 1
    if mid == e:
        print(mid)
        break
