# 시리얼 번호

from sys import stdin
input = stdin.readline

def digit_sum(s):
    res = 0
    for i in s:
        if i.isdigit():
            res += int(i)
    return res

N = int(input())

ans = []
for i in range(N):
    ans.append(input().rstrip())
    
ans.sort(key= lambda x: (len(x), digit_sum(x), x))

print(*ans, sep="\n")