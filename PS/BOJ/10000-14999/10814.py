from sys import stdin
input = stdin.readline

dct = {}
N = int(input())
lst = list(input().split() for _ in range(N))

for i in range(N):
    lst[i][0] = int(lst[i][0])

lst.sort(key=lambda lst: lst[0])

for i in lst:
    print(i[0], i[1])