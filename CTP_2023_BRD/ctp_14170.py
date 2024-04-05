# Counting Haybales

from sys import stdin
from bisect import bisect_left, bisect_right
input = stdin.readline

N, Q = map(int, input().split())

position = list(map(int, input().split()))

position.sort()

# def lower_bound(lst, target):
#     left, right = 0, len(lst)
#     while left < right:
#         mid = left + (right - left) //2
#         if lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid
#     return right


for i in range(Q):
    A, B = map(int, input().split())
    one = bisect_left(position, A)
    two = bisect_right(position, B)
    #print(f"one : {one} two : {two}")

    print(f"{two - one}")


