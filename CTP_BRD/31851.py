# 벽록의 가면
# 2024-05-24
# 기하학

import itertools

def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def is_convex_quad(p1, p2, p3, p4):
    # Check all permutations to ensure convexity
    points = [p1, p2, p3, p4]
    for order in itertools.permutations(points):
        cross_products = [
            cross_product(order[0], order[1], order[2]),
            cross_product(order[1], order[2], order[3]),
            cross_product(order[2], order[3], order[0]),
            cross_product(order[3], order[0], order[1])
        ]
        if all(cp > 0 for cp in cross_products) or all(cp < 0 for cp in cross_products):
            return True
    return False

def count_convex_quads(points):
    quad_combinations = list(itertools.combinations(points, 4))
    convex_quad_count = sum(1 for quad in quad_combinations if is_convex_quad(*quad))
    return convex_quad_count

# 입력 받기
N = int(input().strip())
points = [tuple(map(int, input().strip().split())) for _ in range(N)]

# 불록한 사각형의 개수 계산
result = count_convex_quads(points)

# 결과 출력
print(result)