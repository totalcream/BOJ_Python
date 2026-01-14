# 두 배열의 합

from sys import stdin
from bisect import bisect_left, bisect_right
input = stdin.readline

T = int(input())
N = int(input())
n_lst = list(map(int, input().split()))
M = int(input())
m_lst = list(map(int, input().split()))

n_sum, m_sum = n_lst, m_lst

for i in range(N):
    for j in range(i + 1, N):
        n_sum.append(sum(n_lst[i:j+1]))

for i in range(M):
    for j in range(i + 1, M):
        m_sum.append(sum(m_lst[i:j+1]))

n_sum.sort()
m_sum.sort()

rst = 0
for i in range(len(n_sum)):
    l = bisect_left(m_sum, T - n_sum[i])
    r = bisect_right(m_sum, T - n_sum[i])
    rst += r - l

print(rst)