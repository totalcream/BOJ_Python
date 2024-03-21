#조각 케이크

from sys import stdin, setrecursionlimit
input = stdin.readline

setrecursionlimit(10**6)
def make(pos, val):
    global N
    if pos == N:
        if 0.99 <= val <= 1.01:
            return 1
        else:
            return 0
    
    skip = make(pos + 1, val + 0)
    select = make(pos + 1, val + lst[pos])
    return skip + select

N = int(input())
lst = list(map(int, input().split()))
for i in range(len(lst)):
    lst[i] = 1 / lst[i]

print(make(0, 0))