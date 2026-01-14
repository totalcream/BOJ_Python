# 큰 수 만들기

from sys import stdin
from itertools import combinations, permutations
input = stdin.readline

N = int(input())

lst = list(map(str, input().split()))

ans = list(permutations(lst, N))


#print(ans)