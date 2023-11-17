#친구 네트워크
from sys import stdin, setrecursionlimit
input = stdin.readline

setrecursionlimit(1000000)
def find(X):
    if X == parent[X]:
        return X
    else:
        parent[X] = find(parent[X])
        return parent[X]

def merge(X, Y):
    A = find(X)
    B = find(Y)

    if A != B:
        parent[B] = A
        visited[A] += visited[B]

T = int(input())
for _ in range(T):
    F = int(input())

    parent = dict()
    visited = dict()

    for i in range(F):
        A, B = map(str, input().split())
        if A not in parent:
            parent[A] = A
            visited[A] = 1
        if B not in parent:
            parent[B] = B
            visited[B] = 1
    
        merge(A, B)
        print(visited[find(A)])
