#트럭
from sys import stdin
input = stdin.readline

N, W, L = map(int, input().split())
trucks = list(map(int, input().split()))

cnt = 0
gogo = [0] * W

while gogo:

    cnt += 1
    gogo.pop(0)
    if trucks:
        if sum(gogo) + trucks[0] <= L:
            gogo.append(trucks.pop(0))
        else:
            gogo.append(0)

print(cnt)