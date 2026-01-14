# 문자열 접기
# 2024-05-24
# 전체 탐색

from sys import stdin
input = stdin.readline

def max_folding_score(s):
    n = len(s)
    max_score = 0
    
    for i in range(1, n):
        left = s[:i][::-1]
        right = s[i:]
        score = sum(1 for x, y in zip(left, right) if x == y)
        max_score = max(max_score, score)
    
    return max_score

N = int(input())
string = input().strip()
Q = int(input())

for _ in range(Q):
    L, R = map(int, input().split())
    print(max_folding_score(string[L-1:R]))