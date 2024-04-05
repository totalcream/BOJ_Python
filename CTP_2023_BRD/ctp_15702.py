#중간고사 채점

from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

points = list(map(int, input().split()))

lst = []
ans = []
for i in range(M):
    lst.append(list(map(str, input().split())))

for i in lst:
    num = int(i[0])
    point = 0
    for idx, j in enumerate(i[1:]):
        if j == 'O':
            point += points[idx]
    
    ans.append((num, point))

b = sorted(ans, key=lambda x : (x[1], -x[0]))
print(*b[-1])