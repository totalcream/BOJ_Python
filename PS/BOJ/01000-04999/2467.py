# 용액

from sys import stdin
input = stdin.readline

N = int(input())
lst = list(map(int, input().split()))

lst.sort()

left, right = 0, N-1
ans = 2e9
case = []
while left < right:
    Sum = lst[left] + lst[right]
    if abs(Sum) < ans:
        ans = abs(Sum)
        case = [lst[left], lst[right]]
    if Sum < 0:
        left += 1
    else:
        right -= 1

print(case[0], case[1])