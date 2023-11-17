#단지번호붙이기
from sys import stdin, setrecursionlimit
input = stdin.readline

setrecursionlimit(1000000)

N = int(input())
Map = [list(map(int, input().rstrip())) for _ in range(N)]

#상하좌우
dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]
cnt = 0
ans = []
def DFS(Map, x, y):
    global cnt
    #현재 노드를 방문 처리
    Map[y][x] = 0
    cnt += 1
    #print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for dx, dy in dir:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N and Map[ny][nx]:
            DFS(Map, nx, ny)
    return cnt
for y in range(N):
    for x in range(N):
        if Map[y][x]:
            cnt = 0
            ans.append(DFS(Map, x, y))

print(len(ans))
for a in sorted(ans):
    print(a)



