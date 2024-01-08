# N과 M(2)
from sys import stdin
from itertools import combinations, permutations
input = stdin.readline


N, M = map(int, input().split())
lst = [i+1 for i in range(N)]

res = list(combinations(lst, M))

for case in res:
    for i in case:
        print(i, end=" ")
    print()