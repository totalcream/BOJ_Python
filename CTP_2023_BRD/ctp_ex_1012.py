import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    #상하좌우 확인을 위해 dx dy 생성
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if(0 <= nx < M) and (0 <= ny < N):
            if graph[ny][nx] == 1:
                graph[ny][nx] = -1
                dfs(nx, ny)

T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*M for i in range(N)]
    cnt = 0

    for j in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1

    for x in range(M):
        for y in range(N):
            if graph[y][x] == 1:
                dfs(x, y)
                cnt +=  1
    print(cnt)
