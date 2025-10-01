# 오큰수
# 2024-09-19


from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
answer = [-1 for _ in range(N)]
temp = deque([])


temp.append(0)
for i in range(1,N):
  if temp and A[temp[-1]] >= A[i]:
    temp.append(i)
    
  while temp and A[temp[-1]] < A[i]:
    answer[temp.pop()] = A[i]
  temp.append(i)

for i in answer:
  print(i, end = " ")