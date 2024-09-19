#AC
from sys import stdin
input = stdin.readline
from collections import deque

T = int(input())
# case = deque()
# for _ in range(T):
#     fnc = input().rstrip()
#     num = int(input())
#     lst = input().rstrip()[1:-1]
#     case.append([fnc, num, lst])

while T != 0:
    #fnc, num, lst = case.popleft()
    fnc = input().rstrip()
    num = int(input())
    lst = input().rstrip()[1:-1].split(",")
    revcnt = 0
    tmplst = deque(lst)
    if num == 0:
        tmplst = []
    error = False
    for i in fnc:
        if i == 'R':
            revcnt += 1
        elif i == 'D':
            if len(tmplst) < 1:
                print("error")
                error = True
                break
            else:
                if revcnt % 2 == 0:
                    tmplst.popleft()
                else:
                    tmplst.pop()

    T -= 1
    if error is False:
        if revcnt % 2 == 0:
            print("[" + ",".join(tmplst) + "]")
        else:
            tmplst.reverse()
            print("[" + ",".join(tmplst) + "]")