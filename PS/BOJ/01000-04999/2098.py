# 외판원 순회

from sys import stdin
input = stdin.readline

# 쉬프트 연산 하는 법
# 방문한 도시 추가하기
# visited | (1 << next) # next: 현재 방문할 도시
# 방문했는지 확인하기 0
# visited & (1 << next) # next: 현재 방문할 도시

# 모든 도시에 방문했는지 확인하기
# visited == (1 << N) - 1 # N: 도시의 개수

N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dp = {}

def dfs(now, visited):
    # 모든 도시를 방문한 경우
    if visited == (1 << N) - 1:
        # 다시 출발 도시로 갈 수 있는 경우 출발 도시까지의 비용 반환
        if board[now][0]:
            return board[now][0]
        else:
            # 갈 수 없는 경우 무한대를 반환(이 경로는 최소비용이 아님)
            return int(1e9)
        

    # 이전에 계산된 경우 결과 반환
    if (now, visited)in dp:
        # now까지 방문한 최소 비용
        return dp[(now, visited)]
    
    min_val = int(1e9)
    for next in range(1, N):
        # 비용이 0이어서 못가거나, 이미 방문한 루트면,
        if board[now][next] == 0 or visited & (1 << next):
            continue
        cost = dfs(next, visited | (1 << next)) + board[now][next]
        min_val = min(cost, min_val)

    # 방문한 경우 중에서 최소 비용이 드는 루트비용 저장
    dp[((now, visited))] = min_val
    return min_val


# 0번 째부터 방문하고, visited 처리
print(dfs(0, 1))