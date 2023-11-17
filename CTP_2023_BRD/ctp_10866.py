import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque()
for _ in range(N):
    tmp = input().split()
    if tmp[0] == "push_front": q.appendleft(int(tmp[1]))
    elif tmp[0] == "push_back": q.append(int(tmp[1]))
    elif tmp[0] == "pop_front":
        if len(q) == 0: print(-1)
        else: print(q.popleft())
    elif tmp[0] == "pop_back":
        if len(q) == 0: print(-1)
        else: print(q.pop())
    elif tmp[0] == "size": print(len(q))
    elif tmp[0] == "empty": print(int(len(q) == 0))
    elif tmp[0] == "front":
        if len(q) == 0: print(-1)
        else: print(q[0])
    else:
        if len(q) == 0: print(-1)
        else: print(q[-1])