from sys import stdin
input = stdin.readline

T = int(input())

for i in range(T):
    N = int(input())

    max = N
    while True:
        if N == 1:
            break
        if N % 2:
            N = N*3 + 1
            if N >= max:
                max = N
        else:
            N = N//2
    print(max)
