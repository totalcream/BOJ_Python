# 가장 긴 증가하는 부분 수열 2
# 가장 긴 증가하는 부분 수열의 순서는 몰라도 되지만
# 수열의 길이만 구하면 된다는 데에 초점을 둔다.

from sys import stdin
from bisect import bisect_left
input = stdin.readline

N = int(input())
seq = list(map(int, input().split()))

LIS = [seq[0]]

for item in seq:
    if LIS[-1] < item:
        LIS.append(item)
    else:
        idx = bisect_left(LIS, item)
        LIS[idx] = item

print(len(LIS))
