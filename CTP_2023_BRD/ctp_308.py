import sys
from queue import PriorityQueue

que = PriorityQueue()

r = int(input())
numbers = list(map(int, input().split()))

print(numbers)

#for _ in range(r):
#    que.put(numbers)
#    print(que)
#PriorityQueueClion