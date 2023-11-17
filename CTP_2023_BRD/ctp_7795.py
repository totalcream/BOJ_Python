from sys import stdin
input = stdin.readline

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    N = list(map(int, input().split()))
    M = list(map(int, input().split()))

    #print(A, B, N, M)
    N.sort()
    M.sort()

    idx = 0
    sum = 0

    for i in range(A):
        while idx < B:
            if N[i] > M[idx]:
                idx += 1
            else:
                break
        sum += idx
    print(sum)

