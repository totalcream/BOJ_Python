# 수 정렬하기 3

from sys import stdin
input = stdin.readline

N = int(input())

dic = {}

for _ in range(N):
    tmp = int(input())

    if tmp in dic:
        dic[tmp] = dic[tmp] + 1
    else:
        dic[tmp] = 1

ans = sorted(dic)

for i in ans:
    cnt = dic[i]
    for j in range(cnt):
        print(i)