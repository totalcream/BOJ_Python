# 카드 교환
# 2024-05-20
# 간단한 그리디
# 하지만 대회 당일에는 뭔가 이상했는지 제대로 작동하지 않았다.
# gpt의 힘을 빌려서 작성해 봄


from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))


sum_max = 0

for _ in range(M):
    if not lst:
        break
    
    max_value = max(lst)
    if max_value > 0:
        sum_max += max_value
        lst.remove(max_value)
    else:
        continue
    
    if not lst:
        break
    
    min_value = min(lst)
    lst.remove(min_value)

print(sum_max)


# ans = 0
# i = 0
# while nlst:
#     if i > M:
#         break
#     highdeq = lst.index(max(lst))
#     # if lst[highdeq] < 0:
#     #     i += 1
#     #     continue                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
#     # else:
#     ans += lst[highdeq]
#     nlst.pop(highdeq)
#     mlst.pop(highdeq)
#     lst.pop(highdeq)
#     # 딜러
#     if nlst == []:
#         break
#     lowdeq = lst.index(min(lst))
#     nlst.pop(lowdeq)
#     mlst.pop(lowdeq)
#     lst.pop(lowdeq)
#     i += 1

# print(ans)