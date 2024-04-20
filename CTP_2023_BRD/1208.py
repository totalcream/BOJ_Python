# 부분수열의 합 2
# 2024-04-18
# 이분탐색으로 풀어도되고(bisect) 직접 구현해서 풀어도 되고
# 왼쪽 오른쪽 배열로 나뉜다음(2**40 => 2 * 2**20)
# 합의 갯수를 찾아서 계산

from sys import stdin
# from bisect import bisect_left, bisect_right
from collections import defaultdict
input = stdin.readline

N, S = map(int, input().split())
seq = list(map(int, input().split()))

cnt = 0
summ_dict = defaultdict(int)

def right_search(mid, partial_sum):
    if mid == N:
        summ_dict[partial_sum] += 1
        return

    right_search(mid + 1, partial_sum)
    right_search(mid + 1, partial_sum + seq[mid])

def left_search(st, partial_sum):
    global cnt
    if st == N//2:
        if summ_dict[S - partial_sum]:
            cnt += summ_dict[S - partial_sum]
        return

    left_search(st + 1, partial_sum)
    left_search(st + 1, partial_sum + seq[st])

right_search(N//2, 0)
left_search(0, 0)

print(cnt if S else cnt-1)