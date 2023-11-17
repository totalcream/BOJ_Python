from sys import stdin
input = stdin.readline
import math
# math.inf
N = int(input())
#graph = [[math.inf]*N]
graph = []
for i in range(N-1, 0, -1): # if N is 4 -> 3, 2, 1, ...
    info = list(map(int, input().split()))
    graph.append(info)

print(graph)

res = 0

for i, idx in enumerate(graph):
    if idx > i.index(max(i)):
        res += max(i)

print(res)
