import sys
from collections import deque
input = sys.stdin.readline

st = deque()
for _ in range(int(input())):
    tmp = input().split()
    if tmp[0] == "push": st.append(int(tmp[1]))
    elif tmp[0] == "pop":
        if len(st) == 0: print(-1)
        else: print(st.pop())
    elif tmp[0] == "size": print(len(st))
    elif tmp[0] == "empty": print(int(len(st) == 0))
    else:
        if len(st) == 0: print(-1)
        else: print(st[-1])