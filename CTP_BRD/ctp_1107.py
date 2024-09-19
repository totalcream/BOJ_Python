from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())
brokenN = list(map(str, input().split()))

cnt = abs(100 - N)

for i in range(1000001):
    for j in str(i):
        if j in brokenN:
            break
    
    else:
        cnt = min(cnt, len(str(i)) + abs(i - N))

print(cnt)