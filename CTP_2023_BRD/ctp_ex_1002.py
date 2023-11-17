import math

result = 0
T = int(input())
case = [list(map(int, input().split())) for _ in range(T)]

for i in range(T):
    dis = math.sqrt(abs(case[i][0] - case[i][3])**2 + abs(case[i][1] - case[i][4])**2)

    #두 원의 중심이 같은 경우
    if dis == 0:
        if case[i][2] == case[i][5]: # 두 원의 크기가 같음
            result = -1
        else: # 원 하나가 안에 껴있을 경우
            result = 0
    else: # 두 원의 중심이 다름
        if case[i][2] + case[i][5] == dis or abs(case[i][2] - case[i][5]) == dis: # 원 하나가 내접, 다른 원 하나는 외접
            result = 1
        elif abs(case[i][2] - case[i][5]) < dis < case[i][2] + case[i][5]: # 두 원이 다른 중심, 두 점에서 만남
            result = 2
        else: # 겹치는 경우가 없음
            result = 0
    print(result)