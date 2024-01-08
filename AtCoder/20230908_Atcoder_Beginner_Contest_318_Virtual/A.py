from sys import stdin
input = stdin.readline

N, M, P = map(int, input().split())
cnt = 0
sumP = P
for i in range(1, N+1):
    if i == M:
        cnt += 1
    elif i == M + sumP:
        cnt += 1
        sumP += P

print(cnt)