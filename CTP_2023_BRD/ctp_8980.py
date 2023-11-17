import sys

N, C = map(int, input().split())
M = int(input())
case = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]

case.sort()
print(case)

result = 0
box = 0
for i, v in enumerate(case):
    box += v[2]
    