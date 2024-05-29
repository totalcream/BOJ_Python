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


# # 최적이진트리 코드
# def optsearchtree(p):
#     n = len(p) - 1
#     A = [[-1] * (n + 1) for _ in range(n + 2)] # 최소 비용 저장
#     R = [[-1] * (n + 1) for _ in range(n + 2)] # 루트노드를 저장함
#     for i in range(1, n + 1):
#         A[i][i - 1] = 0
#         A[i][i] = p[i]
#         R[i][i - 1] = 0
#         R[i][i] = i # 한개밖에 없으면 자기 자신이 루트임
#         # 초기화 과정
#     A[n + 1][n] = 0
#     R[n + 1][n] = 0
#     for diagonal in range(1, n): # 대각선을 중심대각선부터 마지막 대각선까지 반복함
#         for i in range(1, n - diagonal + 1): # 대각선 안에서의 이동
#             j = i + diagonal # 현재 diagonal에서 몇번째 원소인지를 결정함, 1번 대각선은 이미 자기자신으로 설정되어있음
#             A[i][j], R[i][j] = minimum(A, p, i, j)
#     return A, R
    
# def minimum (A, p, i, j):
#     minValue = INF
#     minK = 0
#     for k in range(i, j + 1):
#         value = A[i][k - 1] + A[k + 1][j]
#         for m in range(i, j + 1):
#             value += p[m] # summation of p[m], 즉 지금까지 모든 k 서치값의 합
#         if (minValue > value):
#             minValue = value
#             minK = k 
#     return minValue, minK # 최소값 찾아서 반납

# # 플로이드 워셜 알고리즘
# import sys
# input = sys.stdin.readline

# n = int(input())
# v = int(input())
# INF = 9999999
# graph = [[INF] * (n+1) for _ in range(n+1)]

# for _ in range(v) :
#     v1, v2, c = map(int, input().split())
#     graph[v1][v2] = c
    
# for i in range(1, n+1) :
#     graph[i][i] = 0

# for k in range(1, n+1) :
#     for i in range(1, n+1) :
#         for j in range(1, n+1) :
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            

# for i in range(1, n+1) :
#     for j in range(1, n+1) :
#         if graph[i][j] == INF :
#             print("0", end=" ")
#         else :
#             print(graph[i][j], end=" ")
#     print()

# # 트리의 지름 - 가중치없음

# import sys
# from collections import deque
# input = sys.stdin.readline

# V = int(input())
# tree = [[] for _ in range(V+1)]
# # 2차원 리스트에 트리 저장(연결 그래프)
# for _ in range(V):
#     line = list(map(int, input().split()))
#     cnt_node = line[0]
#     idx = 1
#     while line[idx] != -1:
#         adj_node, adj_cost = line[idx], line[idx+1]
#         tree[cnt_node].append((adj_node, adj_cost))
#         idx += 2

# def BFS(start):
#     q = deque()
#     q.append((start, 0))
#     visited = [-1]*(V+1)
#     visited[start] = 0
#     res = [0, 0] # start로부터 가장 먼 거리에 있는 노드와 거리 값
    
#     while q:
#         cnt_node, cnt_dist = q.popleft()
        
#         for adj_node, adj_dist in tree[cnt_node]:
#             if visited[adj_node] == -1:
#                 cal_dist = cnt_dist + adj_dist
#                 q.append((adj_node, cal_dist))
#                 visited[adj_node] = cal_dist
#                 if res[1] < cal_dist:
#                     res[0] = adj_node
#                     res[1] = cal_dist
        
#     return res
    
# # 트리 지름 공식 참고
# # u-v가 지름이라고 하자. 임의의 점 x에서 가장 먼 거리의 노드 y는
# # 반드시 u 또는 v이다. 따라서 y에서 BFS를
# # 한번 더 해주면 지름을 구할 수 있다.
# point, _ = BFS(1)
# print(BFS(point)[1])


# # 색상환

# import sys

# mod = 1000000003
# n = int(sys.stdin.readline())
# k = int(sys.stdin.readline())

# dp = [[0] * (k + 1) for _ in range(n + 1)]

# for i in range(n + 1):
#     dp[i][0] = 1
#     dp[i][1] = i

# for i in range(2, n + 1):
#     for j in range(2, k + 1):
#         if i == n:
#             dp[i][j] = dp[i - 3][j - 1] + dp[i - 1][j]
#         else:
#             dp[i][j] = dp[i - 1][j] + dp[i - 2][j - 1]
#         dp[i][j] %= mod

# print(dp[n][k])

# # 쉬운 계단 수

# N = int(input())

# dp = [[0]*10 for _ in range(N+1)]
# for i in range(1, 10):
#     dp[1][i] = 1

# MOD = 1000000000

# for i in range(2, N+1):
#     for j in range(10):
#         if j == 0:
#             dp[i][j] = dp[i-1][1]
#         elif j == 9:
#             dp[i][j] = dp[i-1][8]
#         else:
#             dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] 

# print(sum(dp[N]) % MOD)

def matrix_chain_order(p):
    n = len(p) - 1
    M = [[0 for x in range(n)] for y in range(n)]
    P = [[0 for x in range(n)] for y in range(n)]
    
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            M[i][j] = float('inf')
            for k in range(i, j):
                q = M[i][k] + M[k+1][j] + p[i]*p[k+1]*p[j+1]
                if q < M[i][j]:
                    M[i][j] = q
                    P[i][j] = k
    
    return M, P

# 주어진 행렬 차원
p = [10, 4, 5, 20, 2, 50]

# 최소 곱셈 수와 최적 곱셈 순서 계산
M, P = matrix_chain_order(p)

import pandas as pd
import ace_tools as tools

# 테이블 형식으로 출력
M_df = pd.DataFrame(M, columns=[f'A{i+1}' for i in range(len(p)-1)], index=[f'A{i+1}' for i in range(len(p)-1)])
P_df = pd.DataFrame(P, columns=[f'A{i+1}' for i in range(len(p)-1)], index=[f'A{i+1}' for i in range(len(p)-1)])

tools.display_dataframe_to_user(name="Matrix M Table", dataframe=M_df)
tools.display_dataframe_to_user(name="Matrix P Table", dataframe=P_df)

M_df, P_df

# 24479
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, r = map(int, input().split()) # 정점의 수, 간선의 수, 시작 정점
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1) # 방문 순서 저장. 0이면 방문 X

c = 1
def dfs(graph, v, visited):
    global c
    visited[v] = c # 방문하면 순서 나타내기
    
    for i in graph[v]:
        if visited[i] == 0: # 방문 안한 노드이면
            c += 1
            dfs(graph, i, visited) # dfs 재귀
            
# m개의 연결된 간선 정보 입력받기
for i in range(m):
    a, b = (map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

for i in range(n+1): # 오름차순으로 인접노드 방문하기 위해 정렬
    graph[i].sort()
# print(graph)

dfs(graph, r, visited)

for i in range(1, n+1):
    print(visited[i])


# 24480
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m,r = map(int,input().split())
link = [[] for _ in range(n+1)]
ans = [0]*(n+1)
cur = 1

for _ in range(m):
    a,b = map(int,input().split())
    link[a].append(b)
    link[b].append(a)
for lst in link:
    lst.sort(reverse = True)

def dfs(v):
    global cur
    ans[v] = cur
    for to_v in link[v]:
        if ans[to_v]:
            continue
        cur+=1
        dfs(to_v)
dfs(r)
for i in ans[1:]:
    print(i)

# 24444

import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, r = map(int, input().split()) # 정점의 수, 간선의 수, 시작 정점
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1) # 방문 순서 저장. 0이면 방문 X

c = 1 # 순서
def bfs(graph, start, visited):
    global c
    queue = deque([start])
    visited[start] = c # 방문하면 순서 나타내기
    
    while queue:
        v = queue.popleft()
        for i in graph[v]: # 인접 노드 중
            if visited[i] == 0: # 방문하지 않은 노드 큐에 추가
                queue.append(i)
                c += 1 # 순서+1
                visited[i] = c

# m개의 연결된 간선 정보 입력받기
for i in range(m):
    a, b = (map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

for i in range(n+1): # 인접노드 정보 오름차순 정렬
    graph[i].sort()
# print(graph)

bfs(graph, r, visited)

for i in range(1, n+1):
    print(visited[i])


# 24445

from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
count = 1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    global count

    q = deque([r])
    visited[r] = 1
    while q:
        v = q.popleft()
        graph[v].sort(reverse=True)
        for g in graph[v]:
            if visited[g] == 0:
                count += 1
                visited[g] = count
                q.append(g)
bfs(r)

for v in visited[1:]:
    print(v)

