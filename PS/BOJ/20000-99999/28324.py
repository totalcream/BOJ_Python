# 스케이트 연습
# 2024-06-07
# 그리디 알고리즘

from sys import stdin
input = stdin.readline

N = int(input())
V = []
temp = input().rstrip().split(" ")

for i in range(N-1, -1, -1):
    V.append(int(temp[i]))

answer = 1
cur_speed = 1

for i in range(1, N):

    if V[i] > cur_speed:
        cur_speed += 1
    else:
        cur_speed = V[i]

    # print(cur_speed)
    answer += cur_speed

print(answer)