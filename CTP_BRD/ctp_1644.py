# 소수의 연속합

from sys import stdin
import math
input = stdin.readline

N = int(input())

if N == 1:
    print(0)
    exit(0)
elif N == 2:
    print(1)
    exit(0)
elif N == 3:
    print(1)
    exit(0)

def prime_numbers(n):
    arr = [i for i in range(n+1)]
    end = int(n**(1/2))
    for i in range(2, end+1):
        if arr[i] == 0: 
            continue
        for j in range(i*i, n+1, i):
            arr[j] = 0
            
    return [i for i in arr[2:] if arr[i]]

lst = prime_numbers(N)
left, right = 0, 0
cnt = 0
length = len(lst)
while right <= length and left <= right:
    Sum_lst = lst[left:right]
    total = sum(Sum_lst)
    if total == N:
        cnt += 1
        right += 1
    elif total < N:
        right += 1
    else:
        left += 1

print(cnt)