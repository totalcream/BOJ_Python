#1940 주몽

N = int(input())
M = int(input())
case = sorted(map(int, input().split()))

i, j = 0, N-1
result = 0

while i != j:
    w = case[i] + case[j]
    if w == M:
        result += 1
        i += 1
    elif w > M:
        j -= 1
    else:
        i += 1

print(result)