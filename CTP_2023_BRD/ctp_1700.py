# from sys import stdin
# input = stdin.readline

# from collections import deque
# from queue import PriorityQueue

# N, K = map(int, input().split())
# plugs = deque(map(int, input().split()))

# cnt = 0
# lst = deque(maxlen=N)

# #print(plugs)
# while plugs:
#     tmp = plugs.popleft()

#     if len(lst) == 0:
#         lst.append(tmp)
#     elif len(lst) != 0:
#         if len(lst) >= N:
#             if tmp in lst:
#                 pass
#             elif tmp not in plugs:
#                 lst.pop()
#                 cnt += 1
#                 lst.append(tmp)
#         else:
#             if tmp in lst:
#                 pass
#             else:
#                 lst.append(tmp)
#     print(lst, cnt, tmp)

# print(cnt)

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
products = list(map(int, input().split()))

multi_tab = [0] * N
ans = 0
change = maximum = 0

while products:
    product = products[0]
    if product in multi_tab:
        products.remove(product)   
        continue

    elif 0 in multi_tab:
        multi_tab[multi_tab.index(0)] = product
        products.remove(product)

    else:
        for mt in multi_tab:
           
            if mt not in products:
                change = mt
                break

            elif products.index(mt) > maximum:
                maximum = products.index(mt)
                change = mt

        multi_tab[multi_tab.index(change)] = product
        products.remove(product)
        maximum = 0
        ans += 1

print(ans)
