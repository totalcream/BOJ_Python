# 나무 자르기

from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

treelen = list(map(int, input().split()))

s, e = 1, max(treelen)

while s <= e:
    ans = 0
    mid = (s + e) // 2

    for i in treelen:
        if i > mid:
            ans += i - mid
    
    if ans < M:
        e = mid - 1
    else:
        s = mid + 1

print(e)