#마왕의 성 
from sys import stdin
input = stdin.readline
from collections import deque

def find(X):
    if lst[X] != X:
        lst[X] = find(lst[X])
    return lst[X]

def merge(X, Y):
    A, B = find(X), find(Y)
    lst[A] = B

def isUnion(X, Y):
    A, B = find(X), find(Y)
    # if A == B:
    #     print('YES')
    # else:
    #     print("NO")
    
N, M = map(int, input().split())

lst = []
area = []
for i in range(N):
    tmp = list(map(int, input().split()))
    area.append(tmp)

tax = []
for i in range(N):
    tmp = list(map(int, input().split()))
    tax.append(tmp)

#(Y, X) coordinates
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

area.sort()
lst = [_ for _ in range(1, N*M+1)]

print(lst)


# dq = deque()
# total = []
# for i in range(N):
#     total.append([0] * M)
# #print(area[0][2] >= area[0][3])
# for i in range(N):
#     for j in range(M):
#         visited = [[False] * M] * N
#         dq.append((i, j))
#         while dq:
#             y, x = dq.pop()
#             for dy, dx in dir:
#                 nx = x + dx
#                 ny = y + dy

#                 if 0 <= nx < M and 0 <= ny < N and area[y][x] >= area[ny][nx] and visited[ny][nx] is False:
#                     total[y][x] += tax[ny][nx]
#                     visited[y][x] = True
#                     dq.append((ny, nx))
#                     #print(total, i, j)

# tmp = deque()
# visited = [[False] * M] * N
# def find_area(y, x):
#     visited[y][x] = True
#     for dy, dx in dir:
#         nx = x + dx
#         ny = y + dy
#         if 0 <= nx < M and 0 <= ny < N and (area[y][x] >= area[ny][nx]) and (visited[ny][nx] is False):
#                 #print(tmp.append((ny, nx)))
#                 find_area(ny, nx)
#     #print(tmp)

# find_area(0, 0)


# for i in total:
#     for j in range(len(i)):
#         print(i[j], end=" ")
#         if j == len(i)-1:
#             print()
