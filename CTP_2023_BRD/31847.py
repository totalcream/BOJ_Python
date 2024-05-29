# 문자열 접기 (Hard)
# 2024-05-24
# 동적계획법

from sys import stdin
input = stdin.readline

def precompute_dp(string):
    n = len(string)
    dp = [[0] * n for _ in range(n)]
    
    # 부분 문자열의 길이를 2부터 n까지 처리
    for length in range(1, n):  # 실제 부분 문자열의 길이는 length+1임
        for i in range(n - length):
            j = i + length
            max_score = 0
            for k in range(1, (length + 1) // 2 + 1):  # k는 1부터 (길이+1)//2까지
                left, right = string[i:i+k], string[j-k+1:j+1]
                score = sum(1 for a, b in zip(left, right) if a == b)
                max_score = max(max_score, score)
            dp[i][j] = max_score
    
    return dp

# 입력 처리
N = int(input())
string = input().strip()
Q = int(input())

# DP 테이블 미리 계산
dp = precompute_dp(string)

# 각 쿼리에 대해 결과 출력
for _ in range(Q):
    L, R = map(int, input().split())
    print(dp[L-1][R-1])