# 기타줄
# 2024-04-30
# 몰>루

N, M = map(int, input().split())

brand = []
ans = 1e9

minset = 1000
minnat = 1000
for i in range(M):
    A, B = map(int, input().split())
    minset = min(minset, A)
    minnat = min(minnat, B)

if minnat * 6 <= minset:
    ans = minnat * N
else:
    ans = minset * (N//6)
    if minnat * (N % 6) <= minset:
        ans += minnat * (N%6)
    else:
        ans += minset
print(ans)