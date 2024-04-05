# 두 수의 합

from sys import stdin
input = stdin.readline

N = int(input())
lst = list(map(int, input().split()))
M = int(input())

left, right = 0, N-1
cnt = 0
lst.sort()
while left < right:
    Sum = lst[left] + lst[right]
    if Sum == M:
        cnt += 1
        left += 1
    elif Sum < M:
        left += 1
    else:
        right -= 1
print(cnt)