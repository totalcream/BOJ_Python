from sys import stdin
input = stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
lst = list(map(int, input().split()))

pre_score = [0] * N
for i in range(N):
    pre_score[i] = A[i%N] * A[(i+1)%N] * A[(i+2)%N] * A[(i+3)%N]

pre_sum = sum(pre_score)
for i in lst:
    for j in range(4):
            pre_score[i - j - 1] = -pre_score[i - j - 1]
            pre_sum += 2 * pre_score[i - j - 1]
    print(pre_sum)