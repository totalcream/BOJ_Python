N = int(input())
left = 0
for i in range(N):
    A, B = map(int, input().split())
    left += (B % A)

print(left)

