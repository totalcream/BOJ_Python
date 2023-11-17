#해밍 거리
from sys import stdin
input = stdin.readline

N = int(input())

for i in range(N):
    A = input()
    B = input()
    
    cnt = 0
    for i, j in zip(A, B):
        if i != j:
            cnt += 1

    print(f"Hamming distance is {cnt}.")