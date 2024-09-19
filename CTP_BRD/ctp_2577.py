#숫자의 개수
from sys import stdin
input = stdin.readline

lst = []
for _ in range(3):
    lst.append(int(input()))

lst[0] = lst[0]*lst[1]*lst[2]

tmp = str(lst[0])
ans = [0 for _ in range(10)]

for i in tmp:
    ans[int(i)] += 1

for i in ans:
    print(i)