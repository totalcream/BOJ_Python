#집합의 표현
#잘 작동은 함 메모리 초과 코드
#로직은 유니온 파인드의 구조 모방
# from sys import stdin
# input = stdin.readline

# N, M = map(int, input().split())

# lst = []
# for i in range(N+1):
#     tmp = set([i])
#     lst.append(tmp)

# for i in range(M):
#     F, A, B = map(int, input().split())
#     if F:
#         if B in lst[A]:
#             print("YES")
#         else:
#             print("NO")
#     else:
#         print(lst[A].add(B))

#집합의 표현
from sys import stdin, setrecursionlimit
input = stdin.readline

setrecursionlimit(1000000)
N, M = map(int, input().split())

lst = [i for i in range(N+1)]

def find(X):
    if lst[X] != X:
        lst[X] = find(lst[X])
    return lst[X]

def merge(X, Y):
    A = find(X)
    B = find(Y)
    lst[A] = B

def isUnion(X, Y):
    A = find(X)
    B = find(Y)
    if A == B:
        print('YES')
    else:
        print("NO")

for i in range(M):
    F, A, B = map(int, input().split())
    if F:
        isUnion(A, B)
    else:
        merge(A, B)