# RGB 거리
# 2024-05-01
# DP문제
# 0번째는 건너 뛰고 1번째부터 최솟값들을 더해 나간다
# 빨간색의 경우는 초록과 파랑 중 최솟값을 고르고 자기자신을 더해 갱신
# N번째까지 갱신하면서 마지막 다 더해진 N-1번째의 최솟값을 출력

from sys import stdin
input = stdin.readline

N = int(input())
seq = []
for i in range(N):
    seq.append(list(map(int, input().split())))

for i in range(1, N):
    seq[i][0] = min(seq[i-1][1], seq[i-1][2]) + seq[i][0]
    seq[i][1] = min(seq[i-1][0], seq[i-1][2]) + seq[i][1]
    seq[i][2] = min(seq[i-1][0], seq[i-1][1]) + seq[i][2]

print(min(seq[N-1]))