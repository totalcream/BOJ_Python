from collections import deque

n = int(input())
ls = [list(input()) for i in range(n)]
result = 0
for words in ls:
    ip = deque()
    for j in words:
        if(len(ip)) == 0:
            ip.append(j)
        elif len(ip) >= 1:
            if ip[-1] == j:
                ip.pop()
            else:
                ip.append(j)
    if len(ip) == 0:
        result += 1
print(result)