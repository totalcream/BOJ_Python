#벌집
from sys import stdin
input = stdin.readline

N = int(input())

num_piledup = 1
cnt = 1
while N > num_piledup:
    num_piledup += 6 * cnt
    cnt += 1

print(cnt)