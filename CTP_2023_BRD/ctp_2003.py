# 수들의 합 2

from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0

left, right = 0, 1
while right <= N and left <= right:
    sum_lst = lst[left:right]
    total = sum(sum_lst)
    
    if total == M:
        cnt += 1
        right += 1
    elif total < M:
        right += 1
    else:
        left += 1
        
print(cnt)