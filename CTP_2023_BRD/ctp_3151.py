# 합이 0

from sys import stdin
from bisect import bisect_left, bisect_right
input = stdin.readline

N = int(input())

lst = list(map(int, input().split()))

lst.sort()
cache = set(lst)
ans = 0
for i in range(N):
    for j in range(i+1, N):
        target = -(lst[i] + lst[j])
        if target in cache:
            ans += bisect_right(lst, target, j+1, N) - bisect_left(lst, target, j+1, N)

print(ans)