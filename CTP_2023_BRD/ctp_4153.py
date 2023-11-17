from sys import stdin
input = stdin.readline

while True:
    A, B, C = map(int, input().split())
    if (A and B and C) == 0:
        break

    lst = sorted([A, B, C])
    if lst[0]**2 + lst[1]**2 == lst[2]**2:
        print('right')
    else:
        print('wrong')
