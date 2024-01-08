from sys import stdin
input = stdin.readline

H, W = map(int, input().split())

# graph = [[]] * (N+1)
# visited = [False] * (N+1)

board = [[0]*W] * H
dir = [(1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)]

for i in range(H):
    lst = list(map(str, input().split()))
    


print(board)

#empty = [(n, m) for n in range(H) for m in range(W) if board[n][m] == '.']
    # 벽을 세울 수 있는 빈 공간 정보를 리스트에 저장
#print(empty)
    #empty = [(n, m) for n in range(N) for m in range(M) if board[n][m] == 0]
    #direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    #answer = 0