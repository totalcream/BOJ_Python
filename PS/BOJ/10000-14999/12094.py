import sys
from copy import deepcopy

# 빠른 입력을 위한 설정
input = sys.stdin.readline

# N: 보드의 크기, board: 초기 보드 상태
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 최종 결과를 저장할 변수
result = 0

def move_left(current_board):
    """
    보드를 왼쪽으로 밀어서 합치는 함수
    """
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        temp_row = []
        # 0이 아닌 숫자들만 임시 리스트에 추가
        for j in range(N):
            if current_board[i][j] != 0:
                temp_row.append(current_board[i][j])
        
        # 합치기 과정
        merged_row = []
        idx = 0
        while idx < len(temp_row):
            if idx + 1 < len(temp_row) and temp_row[idx] == temp_row[idx + 1]:
                merged_row.append(temp_row[idx] * 2)
                idx += 2
            else:
                merged_row.append(temp_row[idx])
                idx += 1
        
        # 결과를 새로운 보드에 반영
        for j in range(len(merged_row)):
            new_board[i][j] = merged_row[j]
            
    return new_board

def rotate_90(current_board):
    """
    보드를 시계 방향으로 90도 회전시키는 함수
    """
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[j][N - 1 - i] = current_board[i][j]
    return new_board

def dfs(current_board, count):
    """
    깊이 우선 탐색으로 모든 경우를 탐색하는 함수
    current_board: 현재 보드 상태
    count: 현재까지 이동한 횟수
    """
    global result
    
    # 10번 이동했으면 최대값 갱신 후 종료
    if count == 10:
        max_val = 0
        for i in range(N):
            for j in range(N):
                if current_board[i][j] > max_val:
                    max_val = current_board[i][j]
        result = max(result, max_val)
        return

    # 4가지 방향(상, 하, 좌, 우)으로 이동
    for _ in range(4):
        # 이동 후의 보드 상태
        next_board = move_left(current_board)
        
        # 보드에 변화가 있을 경우에만 다음 탐색 진행
        if current_board != next_board:
            dfs(next_board, count + 1)
        
        # 다음 방향을 위해 보드를 90도 회전
        current_board = rotate_90(current_board)


# 초기 보드에서 가장 큰 값을 초기 result로 설정
for i in range(N):
    for j in range(N):
        if board[i][j] > result:
            result = board[i][j]

# DFS 시작
dfs(board, 0)

# 결과 출력
print(result)