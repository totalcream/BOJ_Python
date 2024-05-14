# 수영장 사장님
# 2024-05-14
# BFS
# N과 M에 +2씩 더 주고 계산
# 1부터 단면을 잘라서 높이를 계산

from sys import stdin
input = stdin.readline
from collections import deque

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N, M = map(int, input().split())
ans = 0
mat = []
for _ in range(N):
    mat.append(list(map(int, input().split())))

for h in range(1, 10001):
    now = [[0] * (M + 2) for _ in range(N + 2)]
    for i in range(N):
        for j in range(M):
            if mat[i][j] < h:
                now[i + 1][j + 1] = 0
            else:
                now[i + 1][j + 1] = 1
    q = deque([(0, 0)])
    now[0][0] = 1
    while q:
        y, x = q.popleft()
        for dy, dx in dir:
            yy, xx = y + dy, x + dx
            if yy < 0 or yy >= N + 2 or xx < 0 or xx >= M + 2:
                continue
            if now[yy][xx] == 0:
                now[yy][xx] = 1
                q.append((yy, xx))
    for i in range(N + 2):
        for j in range(M + 2):
            if now[i][j] == 0:
                ans += 1

print(ans)

# 아래는 가장 빠른 파이썬 코드
# 한 번쯤 코드를 읽어보자

# import heapq
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# visited = [[0] * m for _ in range(n)]
# heap = []

# pot = []
# for i in range(n):
#     a = list(map(int, input().split()))
#     for j in range(m):
#         if i == 0 or i == n-1 or j == 0 or j == m-1:
#             heapq.heappush(heap, (a[j], i, j))
#             visited[i][j] = 1
            
#     pot.append(a)
    
    
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]


# def sol():
#     answer = 0
    
    
#     while heap:
#         height, x, y = heapq.heappop(heap)
        
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
        
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
            
#             if visited[nx][ny] == 0:
#                 visited[nx][ny] = 1
            
#                 if pot[nx][ny] > height:
#                     heapq.heappush(heap, (pot[nx][ny], nx, ny))
#                 else:
#                     answer += height - pot[nx][ny]
#                     heapq.heappush(heap, (height, nx, ny))
                
#     return answer