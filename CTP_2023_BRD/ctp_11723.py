#집합
from sys import stdin
input = stdin.readline

N = int(input())
lst = set()

for _ in range(N):
    tmp = input().strip().split()

    if len(tmp) == 1:
        if tmp[0] == "all":
            lst = set([i for i in range(1, 21)])
        else:
            lst = set()
    else:
        F, num = tmp[0], tmp[1]
        num = int(num)

        if F == 'add':
            lst.add(num)
        elif F == 'check':
            if num in lst:
                print('1')
            else:
                print('0')
        elif F == 'remove':
            lst.discard(num)
        elif F == 'toggle':
            if num in lst:
                lst.discard(num)
            else:
                lst.add(num)