# 다각형의 면적
# 2024-04-20
# 다각형의 넓이 구하는 공식으로 구하기
# 마지막에 다 더한 뒤 절댓값 적용하기 - 오목다각형 관련 문제인듯?

from sys import stdin
input = stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

lst.append(lst[0])

x = 0
for i in range(N):
    x += lst[i][0] * lst[i+1][1]

y = 0
for i in range(N):
    y += lst[i][1] * lst[i+1][0]

ans = abs((y - x)) / 2
print(ans)
