# from math import gcd

# def simplify_fraction(num, den):
#     if den == 0:
#         raise ValueError("Denominator cannot be zero.")
#     g = gcd(abs(num), abs(den))
#     return num // g, den // g

# def add_or_subtract(A, B, operation):
#     a1, b1, c1, d1 = A
#     a2, b2, c2, d2 = B

#     if d1 != d2:
#         raise ValueError("d values must be the same.")

#     common_denominator = a1 * a2

#     if operation == 'add':
#         b = b1 * a2 + b2 * a1
#         c = c1 * a2 + c2 * a1
#     elif operation == 'subtract':
#         b = b1 * a2 - b2 * a1
#         c = c1 * a2 - c2 * a1
#     else:
#         raise ValueError("Invalid operation")

#     return simplify_fraction(b, common_denominator) + simplify_fraction(c, common_denominator) + (d1,)

# def multiply(A, B):
#     a1, b1, c1, d1 = A
#     a2, b2, c2, d2 = B

#     if d1 != d2:
#         raise ValueError("d values must be the same.")

#     new_a = a1 * a2
#     new_b = b1 * b2 + c1 * c2 * d1
#     new_c = b1 * c2 + b2 * c1

#     return simplify_fraction(new_b, new_a) + simplify_fraction(new_c, new_a) + (d1,)

# def divide(A, B):
#     a1, b1, c1, d1 = A
#     a2, b2, c2, d2 = B

#     if d1 != d2:
#         raise ValueError("d values must be the same.")

#     conjugate_b2 = b2
#     conjugate_c2 = -c2

#     den = b2**2 - c2**2 * d1

#     new_a = a1 * den
#     new_b = b1 * conjugate_b2 + c1 * conjugate_c2 * d1
#     new_c = c1 * conjugate_b2 - b1 * conjugate_c2

#     return simplify_fraction(new_b, new_a) + simplify_fraction(new_c, new_a) + (d1,)

# # 입력을 받음
# A = tuple(map(int, input().split()))
# B = tuple(map(int, input().split()))

# # A + B, A - B, A * B, A / B 계산
# result_add = add_or_subtract(A, B, 'add')
# result_subtract = add_or_subtract(A, B, 'subtract')
# result_multiply = multiply(A, B)
# result_divide = divide(A, B)

# # 결과 출력
# print(*result_add)
# print(*result_subtract)
# print(*result_multiply)
# print(*result_divide)

from sys import stdin
input = stdin.readline

A, B, C = map(int, input().split())

res  = 0
if A != B:
    if B != C:
        if A != C:
            res = max(A, B, C) * 100
        else:
            res = 1000 + A * 100
    else:
        res = 1000 + B * 100
else:
    if B != C:
        res = 1000 + A * 100
    else:
        res = 10000 + A * 1000

print(res)