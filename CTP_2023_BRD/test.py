# #기계오리 연구
# from sys import stdin
# input = stdin.readline
# from itertools import combinations
# import time

# # def combinations(iterable, r):
# #     # combinations('ABCD', 2) --> AB AC AD BC BD CD
# #     # combinations(range(4), 3) --> 012 013 023 123
# #     pool = list(iterable)
# #     n = len(pool)
# #     if r > n:
# #         return
# #     indices = list(range(r))
# #     yield list(pool[i] for i in indices)
# #     while True:
# #         for i in reversed(range(r)):
# #             if indices[i] != i + n - r:
# #                 break
# #         else:
# #             return
# #         indices[i] += 1
# #         for j in range(i+1, r):
# #             indices[j] = indices[j-1] + 1
# #         yield list(pool[i] for i in indices)

# N, K = map(int, input().split())
# case = list(map(int, input().split()))


# start = time.time()
# lst = combinations(case, K)

# # print(type(lst))
# # ans = []
# # for i in lst:
# #     ans.append(sum(i))
# # ans = set(ans)
# # print(ans)

# #print(list(lst))
# ans = []
# for i in lst:
#     tmp = 0
#     for j in i:
#         tmp += j
#         ans.append(tmp)

# ans = set(ans)
# print(len(ans))
# list(ans)
# print(*ans)
# end = time.time()
# print(end - start)

visited = [[0 for _ in range(10)] for _ in range(10)]
print(visited)
dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]
for idx, qwe in enumerate(dir):
    dy, dx = qwe
    print(idx, dy, dx)

a = (1, 2)
b, c = a
print(b, c)
