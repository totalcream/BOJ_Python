from sys import stdin
input = lambda : stdin.readline().strip()

N, P = map(int, input().split())
list = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
line = [[] for _ in range(7)]

for i, j in list:
    if len(line[i]) == 0:
        line[i].append(j)
        cnt += 1
    
    else:
        if j > line[i][-1]:
            line[i].append(j)
            cnt += 1
        elif j == line[i][-1]:
            continue
        else:
            while len(line[i]) != 0 and j < line[i][-1]:
                line[i].pop()
                cnt += 1
            if len(line[i]) != 0 and line[i][-1] == j:
                continue
            line[i].append(j)
            cnt += 1

print(cnt)