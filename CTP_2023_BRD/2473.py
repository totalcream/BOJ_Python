# 세 용액
# 2024-04-22
# 두 용액 이분탐색 응용같음
# 기준 값 하나를 잡고 나머지로 이분탐색 하면 될듯

from sys import stdin
input = stdin.readline

N = int(input())
lst = list(map(int, input().split()))

lst.sort()
ans = 4e9+1

case = []
for i in range(N - 2):
    left, right = i+1, N-1
    while left < right:
        Sum = lst[left] + lst[right] + lst[i]
        if abs(Sum) < ans:
            ans = abs(Sum)
            case = [lst[i], lst[left], lst[right]]
        if Sum < 0:
            left += 1
        elif Sum > 0:
            right -= 1
        else:
            print(case[0], case[1], case[2])
            exit()

print(case[0], case[1], case[2])