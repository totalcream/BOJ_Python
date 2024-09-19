import sys

N = int(input())
case = list(map(int, sys.stdin.readline().rstrip().split()))
case.sort()

target = 1
for i in case:
    if target < i:
        break
    target += i
print(target)