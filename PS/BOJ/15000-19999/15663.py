# N과 M(9)
from sys import stdin
from itertools import combinations, permutations, combinations_with_replacement
input = stdin.readline

N, M = map(int, input().split())

lst = [*map(int, input().split())]
lst.sort()
res = list(permutations(lst, M))
setted = set(res)
setted = list(setted)
setted.sort()
for case in setted:
    for i in case:
        print(i, end=" ")
    print()