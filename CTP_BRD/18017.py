# 총알의 속도

c = 299792458.0

a, b = map(float, input().split())
print(f"{(a+b) / (1 + (a * b) / (c * c))}")