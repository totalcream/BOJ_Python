from sys import stdin
input = stdin.readline

N = int(input())
# N == 도형의 갯수
# x, y의 최대 길이 구하기
# 리스트에 각 좌표 1씩 더하기
# 1이상의 갯수 구하기
x_max = 0
y_max = 0
lst = []
for i in range(N):
    #A, B, C, D = map(int, input().split())
    A = list(map(int, input().split()))
    # A, B = x1 to x2
    # C, D = y1 to t2
    if A[1] > x_max:
        x_max = A[1]
    if A[3] > y_max:
        y_max = A[3]
    lst.append(A)
cnt = 0
grid = [([0]*x_max) for row in range(y_max)]
for i in lst:
    for x in range(i[0], i[1]):
        for y in range(i[2], i[3]):
            grid[y][x] = 1
            
for i in grid:
    for j in i:
        if j == 1:
            cnt += 1

print(cnt)