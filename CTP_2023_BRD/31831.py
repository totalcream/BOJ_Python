N, M = map(int, input().split())
seq = list(map(int, input().split()))

itai = 0
ans = 0
for i in seq:
    itai += i
    if itai >= M:
        ans += 1
    if itai < 0:
        itai = 0

print(ans)