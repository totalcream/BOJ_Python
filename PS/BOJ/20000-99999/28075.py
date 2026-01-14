from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(2)]

cnt = 0
tmp = 0
ans = []
for i in range(N):
    for j in range(2):
        for k in range(3):
            tmp += lst[j][k]
            if tmp >= M:
                cnt += 1
                tmp = 0
                break

print(cnt)