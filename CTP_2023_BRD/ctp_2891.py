# 카약과 강풍
# 2024-04-30
# 몰?루

N, S, R = map(int, input().split())

fracteam = list(map(int, input().split()))
onemoreteam = list(map(int, input().split()))

lst = [3]+ ([1] * N) + [3]

for i in fracteam:
    lst[i] -= 1

for i in onemoreteam:
    lst[i] += 1

ans = 0
# print(lst)
for i in range(1, N+1):
    if lst[i] == 0:
        if lst[i-1] == 2:
            lst[i-1] = 1
            lst[i] = 1
            continue
        if lst[i+1] == 2:
            lst[i+1] = 1
            lst[i] = 1
            continue
    # if lst[i] > 1:
    #     if lst[i-1] == 0:
    #         lst[i-1] += 1
    #         lst[i] -= 1
    #     elif lst[i+1] == 0:
    #         lst[i+1] += 1
    #         lst[i] -= 1
    else:
        continue

# for i in range(1, N):
#     if lst[i] == 0:
#         ans += 1
# print(lst)
# print(ans)
print(lst.count(0))