from sys import stdin
input = stdin.readline

T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    #print(A, B, N, M)
    A.sort()

    idx = 0
    print(A)

    mn = 0
    mx = N-1
    B = sorted(A)

    for j in range(len(A)):
        while mn+1 != mx:
            mid = (mn+mx)//2
            if A[j]+B[mid] == K:
                mx = mid
                mn = mid
                break
            elif A[j] +B[mid] > K:
                mx = mid
            elif A[j] + B[mid] < K:
                mn = mid
