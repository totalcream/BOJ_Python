# 선분 위의 점

from sys import stdin
from bisect import bisect_left, bisect_right
input = stdin.readline

N, M = map(int, input().split())

position = list(map(int, input().split()))
position.sort()

for _ in range(M):
    A, B = map(int, input().split())
    one = bisect_left(position, A)
    two = bisect_right(position, B)

    #print(f"one : {one} two : {two}")
    print(f"{two - one}")