# import sys
# import os

# for i in range(int(sys.stdin.readline())):
#     #입력
#     a,K = map(int,sys.stdin.readline().split())
#     c = sorted(map(int,sys.stdin.readline().split()))
#     #d: 정답 저장 리스트
#     d = []
#     gz = min(c)
#     pz = max(c)
#     for l in range(len(c)):
#         #만약 l과 가장 작은 수를 더해도 K에 가장 작은 d를 더한경우보다 크거나, l과 가장 큰 수를 더해도 b에 가장 작은 d를 뺀 경우와 같을 경우 탐색 건너뜀.
#         if len(d) != 0:
#             if l + gz < K + d[0] or l + pz + d[0] > K:
#                 pass
#             else:
#                 continue
#         #같은 수끼리 더하지 않게 함
#         e = c[:]
#         e.remove(c[l])
#         #이분탐색, 각 수에 대해 합이 가장 가까운 두 수를 찾음
#         mn = 0
#         mx = len(e)-1
#         while mn+1 != mx:
#             mid = (mn+mx)//2
#             if c[l]+e[mid] == K:
#                mx = mid
#                mn = mid
#                break
#             elif c[l] +e[mid] > K:
#                mx = mid
#             elif c[l] + e[mid] < K:
#                 mn = mid
#         #이분탐색으로 나온 가장 가까운 두 수에 대해 계산       
#         dea = abs(c[l]+e[mn]-K)
#         deb = abs(c[l]+e[mx]-K)
#         de = min(dea,deb)
#         #정답 저장하는 수열의 첫번째 값과 과 비교
#         if len(d) == 0 or d[0] > de:
#             #정답 수열의 첫번째 값보다 작다면 정답 수열을 초기화하고 값을 추가.
#             d = [de]
#             if dea == deb:
#                 if mn != mx:
#                     #만약 이분탐색으로 나온 두 수가 같다면 두번 추가
#                     d.append(de)
#             #만약 정답수열의 첫번째 값과 같다면 정답 수열에 추가.
#         elif d[0] == de:
#             if dea == deb:
#                 if mn != mx:
#                     #만약 이분탐색으로 나온 두 수가 같다면 두번 추가
#                     d.append(de)
#             d.append(de)
#     #d의 길이 //2 를 출력.
#     sys.stdout.write(str(len(d)//2)+'\n')

# n, m, v = map(int, input().split())
# graph = [[]] * (n+1)
# visited = [False] * (n+1)

# for _ in range(m):
#   f, t = map(int, input().split())
#   if graph[f] == []:
#     graph[f] = [t]
#   else:
#     graph[f].append(t)
#   if graph[t] == []:
#     graph[t] = [f]
#   else:
#     graph[t].append(f)

# from collections import deque

# def bfs(graph, i, visited):
#   queue= deque()
#   queue.append(i)
#   while queue:
#     value = queue.popleft()

#     if not visited[value]:
#       print(value, end=' ')
#       visited[value] = True
#       for j in graph[value]:
#         queue.append(j)

# bfs(graph, v, visited)

# n, m, v = map(int, input().split())
# matrix = [[0] * (n+1) for _ in range(n+1)]
# visited = [False] * (n+1)

# for _ in range(m):
#   f, t = map(int, input().split())
#   matrix[f][t] = matrix[t][f] = 1
  
# from collections import deque

# def bfs(matrix, i, visited):
#   queue= deque()
#   queue.append(i)
#   while queue:
#     value = queue.popleft()
#     if not visited[value]:
#       print(value, end=' ')
#       visited[value] = True
#       for c in range(len(matrix[value])):
#         if matrix[value][c] == 1 and not visited[c]:
#           queue.append(c)

# bfs(matrix, v, visited)

# def quick_sort(arr):
#     def sort(low, high):
#         if high <= low:
#             return

#         mid = partition(low, high)
#         sort(low, mid - 1)
#         sort(mid, high)

#     def partition(low, high):
#         pivot = arr[(low + high) // 2]
#         while low <= high:
#             while arr[low] < pivot:
#                 low += 1
#             while arr[high] > pivot:
#                 high -= 1
#             if low <= high:
#                 arr[low], arr[high] = arr[high], arr[low]
#                 low, high = low + 1, high - 1
#         return low

#     return sort(0, len(arr) - 1)

# def merge_sort(arr):
#     def sort(low, high):
#         if high - low < 2:
#             return
#         mid = (low + high) // 2
#         sort(low, mid)
#         sort(mid, high)
#         merge(low, mid, high)

#     def merge(low, mid, high):
#         temp = []
#         l, h = low, mid

#         while l < mid and h < high:
#             if arr[l] < arr[h]:
#                 temp.append(arr[l])
#                 l += 1
#             else:
#                 temp.append(arr[h])
#                 h += 1

#         while l < mid:
#             temp.append(arr[l])
#             l += 1
#         while h < high:
#             temp.append(arr[h])
#             h += 1

#         for i in range(low, high):
#             arr[i] = temp[i - low]

#     return sort(0, len(arr))

# from sys import stdin
# input = stdin.readline

# N = int(input())

# dp = [0] * (N + 1)
# MOD = 10007

# if N < 3:
#     print(1)
# else:
#     dp[2] = 1
#     dp[3] = 1
#     for i in range(4, N + 1):
#         if i >= 2:
#             dp[i] = ((dp[i] + dp[i - 2]) % MOD)
#         if i >= 3:
#             dp[i] = ((dp[i] + dp[i - 3]) % MOD)
    
#     print(dp[N])

# import heapq
# def solution(priorities, location):
#     qe = [(idx, pos) for idx, pos in enumerate(priorities)]
#     ans = 0
#     while 1:
#         cur = qe.pop(0)
#         if any(cur[1] < q[1] for q in qe):
#             qe.append(cur)
#         else:
#             ans += 1
#             if cur[0] == location:
#                 return ans
#     return ans

import itertools
import math

def distance(p1, p2):
    # 두 점 사이의 거리를 계산하는 함수
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def is_inside_triangle(point, triangle):
    # 주어진 점이 삼각형 내부에 있는지 여부를 판단하는 함수
    p0, p1, p2 = triangle
    A = 0.5 * (-p1[1]*p2[0] + p0[1]*(-p1[0] + p2[0]) + p0[0]*(p1[1] - p2[1]) + p1[0]*p2[1])
    s = 1/(2*A)*(p0[1]*p2[0] - p0[0]*p2[1] + (p2[1] - p0[1])*point[0] + (p0[0] - p2[0])*point[1])
    t = 1/(2*A)*(p0[0]*p1[1] - p0[1]*p1[0] + (p0[1] - p1[1])*point[0] + (p1[0] - p0[0])*point[1])
    return s > 0 and t > 0 and 1 - s - t > 0

def count_crossings(triangle1, triangle2):
    # 두 삼각형의 경계를 넘는 횟수를 계산하는 함수
    crossings = 0
    for p1, p2 in itertools.product(triangle1, triangle2):
        if distance(p1, p2) > 1:
            crossings += 1
    return crossings

def max_distance_between_triangles(triangle1, triangle2):
    # 두 삼각형 사이의 최대 거리를 계산하는 함수
    max_dist = 0
    for p1, p2 in itertools.product(triangle1, triangle2):
        max_dist = max(max_dist, distance(p1, p2))
    return max_dist

def min_max_distance(N):
    # 주어진 정N각형에 대한 최소 최대 거리를 계산하는 함수
    min_max_dist = float('inf')
    points = [(math.cos(2 * math.pi * i / N), math.sin(2 * math.pi * i / N)) for i in range(N)]
    for triangle1 in itertools.combinations(points, 3):
        for triangle2 in itertools.combinations(points, 3):
            if triangle1 != triangle2:
                crossings = count_crossings(triangle1, triangle2)
                max_dist = max_distance_between_triangles(triangle1, triangle2)
                min_max_dist = min(min_max_dist, max_dist + crossings)
    return min_max_dist

# 정N각형의 변의 수
N = int(input("정N각형의 변의 수를 입력하세요: "))

# 최소 최대 거리 계산
min_max_dist = min_max_distance(N)
print("최소 최대 거리:", min_max_dist)