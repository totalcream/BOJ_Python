# 가장 가까운 세 사람의 심리적 거리

from sys import stdin
input = stdin.readline
from itertools import combinations

T = int(input())

def check(A, B):
    dis = 0
    for i, j in zip(A, B):
        if i != j:
            dis += 1
    return dis

for _ in range(T):
    N = int(input())
    ans = 13
    mbti = input().rstrip().split()
    if N > 32:
        print(0)
    else:
        case = combinations(mbti, 3)
        for a, b, c in case:
            dis = 0
            dis += check(a, b)
            dis += check(b, c)
            dis += check(a, c)

            ans = min(ans, dis)
        print(ans)