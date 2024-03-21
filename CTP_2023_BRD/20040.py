# 사이클 게임

from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
lst = [i for i in range(N)]
end = 0

def find(x):
    if x == lst[x]:
        return x
    else:
        y = find(lst[x])
        lst[x] = y
        return y

def union(x, y, idx):
    global end
    x = find(x)
    y = find(y)
    if x != y:
        lst[max(x, y)] = min(x, y)
    elif end == 0:
        end = idx

for i in range(M):
    A, B = map(int, input().split())
    union(A, B, i + 1)

print(end)