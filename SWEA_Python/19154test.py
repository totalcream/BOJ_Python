from sys import stdin
input = stdin.readline

T = int(input())

for test_case in range(T):
    case = []
    N = int(input())
    for i in range(N):
        him, ji, min = map(int, input().split())
        case.append([him, ji, min])

    Socket_b = [False, False, False]
    sum = 0
    for j in case:
        maxValue = max(j)
        maxValueIndex = j.index(maxValue)
        if maxValueIndex == 0:
            Socket_b[0] = True
            for i in range(3):
                if maxValueIndex == i:
                    continue
                sum += j[i]
        elif maxValueIndex == 1:
            Socket_b[1] = True
            for i in range(3):
                if maxValueIndex == i:
                    continue
                sum += j[i]
        elif maxValueIndex == 2:
            Socket_b[2] = True
            for i in range(3):
                if maxValueIndex == i:
                    continue
                sum += j[i]
    if Socket_b[0] and Socket_b[1] and Socket_b[2]:

        print(f'#{test_case} {sum}')
    else:
        print("-1")
