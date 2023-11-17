import sys
N = int(input())
case = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


for i in case:
    i.sort()
    print(i[-3])