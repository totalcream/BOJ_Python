# 국회의원 선거
# 2024-04-30
# 몰루

from queue import PriorityQueue
import heapq

hq = []

N = int(input())
dasom = int(input())
for i in range(N-1):
    item = int(input())
    heapq.heappush(hq, (-item, item))

ans = 0

cnt = 0
while len(hq) != 0 and dasom <= hq[0][1]:
    top = hq[0][1]
    tmp = heapq.heappop(hq)
    ans += 1
    dasom += 1
    heapq.heappush(hq, ((top-1)*-1, top-1))
    heapq.heapify(hq)

print(ans)
