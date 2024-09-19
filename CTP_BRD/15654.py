# N과 M(5)
from sys import stdin
from itertools import permutations
input = stdin.readline

N, M = map(int, input().split())

lst = [*map(int, input().split())]
lst.sort()
res = list(permutations(lst, M))

for case in res:
    for i in case:
        print(i, end=" ")
    print()