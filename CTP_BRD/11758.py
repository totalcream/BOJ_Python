from sys import stdin
input = stdin.readline

points = []
for _ in range(3):
    points.append(list(map(int, input().split())))

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2 + x2*y3 + x3*y1 - y1*x2 - y2*x3 - y3*x1

result = ccw(points[0][0], points[0][1], points[1][0], points[1][1], points[2][0], points[2][1])

if result > 0:
    print(1)
elif result < 0:
    print(-1)
else:
    print(0)