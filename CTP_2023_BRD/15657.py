# N과 M(8)
from sys import stdin
from itertools import combinations_with_replacement
input = stdin.readline

N, M = map(int, input().split())

lst = [*map(int, input().split())]
lst.sort()
res = list(combinations_with_replacement(lst, M))

for case in res:
    for i in case:
        print(i, end=" ")
    print()