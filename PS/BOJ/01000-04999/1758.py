# 알바생 강호
# 2024-04-30
# 적당히 큰 순으로 정렬하고 팁이 0원 이하일 경우 제외
# 그리고 전부 다 더하기

T = int(input())
Tips = []
for i in range(T):
    Tips.append(int(input()))

Tips.sort(reverse=True)
ans = 0
for i in range(1, T+1):
    tip = (Tips[i-1] - (i -1))
    if tip < 0:
        continue
    else:
        ans += tip

print(ans)