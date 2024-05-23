# 선분 교차 2
# 2024-05-24
# 기하학

from sys import stdin

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class LineSegment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def ccw(self, a, b, c):
        """
        ccw (Counter Clockwise) 값을 계산하여 세 점이 반시계 방향으로 배열되어 있는지 확인
        """
        return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)

    def is_cross(self, other):
        """
        두 선분이 교차하는지 확인
        """
        p1, p2 = self.p1, self.p2
        q1, q2 = other.p1, other.p2

        ccw1 = self.ccw(p1, p2, q1)
        ccw2 = self.ccw(p1, p2, q2)
        ccw3 = self.ccw(q1, q2, p1)
        ccw4 = self.ccw(q1, q2, p2)

        # 두 선분이 일직선상에 있는 경우
        if ccw1 == 0 and ccw2 == 0 and ccw3 == 0 and ccw4 == 0:
            if (min(p1.x, p2.x) <= max(q1.x, q2.x) and min(q1.x, q2.x) <= max(p1.x, p2.x) and
                min(p1.y, p2.y) <= max(q1.y, q2.y) and min(q1.y, q2.y) <= max(p1.y, p2.y)):
                return True
            else:
                return False
        else:
            # 일반적인 경우: 두 선분이 교차하는 경우
            if ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0:
                return True
            else:
                return False

# 입력 받기
input = stdin.readline
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

# 점과 선분 생성
p1 = Point(x1, y1)
q1 = Point(x2, y2)
p2 = Point(x3, y3)
q2 = Point(x4, y4)

line1 = LineSegment(p1, q1)
line2 = LineSegment(p2, q2)

# 교차 여부 출력
if line1.is_cross(line2):
    print(1)
else:
    print(0)
