# 벽록의 가면 (Hard)
# 2024-05-24
# 기하학

def count_convex_quads(points):
    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    n = len(points)
    result = 0

    for i in range(n):
        for j in range(i + 1, n):
            above = 0
            below = 0

            for k in range(n):
                if k == i or k == j:
                    continue
                cp = cross_product(points[i], points[j], points[k])
                if cp > 0:
                    above += 1
                elif cp < 0:
                    below += 1

            result += above * below

    return result // 2

# 입력 받기
N = int(input().strip())
points = [tuple(map(int, input().strip().split())) for _ in range(N)]

# 불록한 사각형의 개수 계산
result = count_convex_quads(points)

# 결과 출력
print(result)
