#중력 큐 
from sys import stdin, stdout
input = stdin.readline
print = stdout.write
from collections import deque

N = int(input())

#덱의 뒤 방향
#state_l = ['left', 'up', 'right', 'down']
back = 0
dq = deque()
ball = 0
wall = 0

for _ in range(N):
    lst = input().rstrip()
    if lst == 'pop':
        if len(dq) != 0:
            tmp = dq.popleft()
            if tmp == 1:
                ball -= 1
            elif tmp == 2:
                wall -= 1
    else:
        F, intel = lst.split()

        if F == 'push':
            if intel == 'b':
                dq.append(1)
                ball += 1
            elif intel == 'w':
                dq.append(2)
                wall += 1
        elif F == 'rotate':
            if intel == 'l':
                back -= 1
            elif intel == 'r':
                back += 1
            if back == 4:
                back = 0
            elif back == -1:
                back = 3
        elif F == 'count':
            if intel == 'b':
                print(f"{ball}\n")
            elif intel == 'w':
                print(f"{wall}\n")
    if back % 2 == 1:
        while (len(dq) != 0 and (dq[0 if back == 1 else len(dq) - 1]) != 2):
            if back == 1:
                dq.popleft()
            else:
                dq.pop()
            ball -= 1
    #print(f"{dq}\n")