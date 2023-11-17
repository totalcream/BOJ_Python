#여행 가자
from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())
lst = [i for i in range(N)]

def find(X):
    if lst[X] != X:
        lst[X] = find(lst[X])
    return lst[X]

def merge(X, Y):
    A, B = find(X), find(Y)
    if A > B:
        lst[A] = B
    else:
        lst[B] = A

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j]:
            merge(i, j)

path = list(map(int, input().split()))
lst = [-1] + lst
start = lst[path[0]]
for i in range(1, M):
    if lst[path[i]] != start:
        print("NO")
        break
else:
    print("YES")