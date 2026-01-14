# 선분 교차
# 2024-05-24
# 기하학
# 선분 교차 2를 먼저 풀어버려서 1은 코드 똑같이 제출함
# 대신에 2는 클래스로 구현했고 1은 함수로 구현함


from sys import stdin
input = stdin.readline

# 세 점 (x1, y1), (x2, y2), (x3, y3)의 방향을 결정하는 함수
def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2 + x2*y3 + x3*y1 - y1*x2 - y2*x3 - y3*x1

# 두 선분 (x1, y1)-(x2, y2)와 (x3, y3)-(x4, y4)가 교차하는지 확인하는 함수
def is_cross(x1, y1, x2, y2, x3, y3, x4, y4):
    # 각각의 ccw 결과를 계산하여 두 선분이 교차하는지 확인
    result1 = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    result2 = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)

    # 두 선분이 일직선상에 있는 경우
    if result1 == 0 and result2 == 0:
        # 선분의 끝점이 겹치는지 확인
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        if x3 > x4:
            x3, x4 = x4, x3
        if y3 > y4:
            y3, y4 = y4, y3

        if x1 <= x4 and x3 <= x2 and y1 <= y4 and y3 <= y2:
            return True
        else:
            return False
    else:
        # 일반적인 경우: 두 선분이 교차하는 경우
        if result1 <= 0 and result2 <= 0:
            return True
        else:
            return False

# 입력 받기
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

# 교차 여부 출력
if is_cross(x1, y1, x2, y2, x3, y3, x4, y4):
    print(1)
else:
    print(0)