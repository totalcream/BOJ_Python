# 가장 긴 증가하는 부분 수열 5
# 2024-04-22
# 이분 탐색이 키 포인트같다
# 

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
print(*LIS)