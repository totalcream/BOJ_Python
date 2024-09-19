# 2배 또는 0.5배

from sys import stdin
input = stdin.readline

N = int(input())
if N > 2:
    print("YES")
    if N % 2:
        lst = [[i, i+1] for i in range(2, N, 2)]
        print("1", end=' ')
    else:
        lst = [[i, i+1] for i in range(1, N, 2)]

    cnt = 1
    for i in lst:
        
        if cnt % 2:
            print(i[1], i[0], end=' ')
        else:
            print(i[0], i[1], end=' ')
        cnt += 1
else:
    print("NO")
