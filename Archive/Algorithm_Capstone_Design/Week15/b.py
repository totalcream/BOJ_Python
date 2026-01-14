def maximize_score(N, T, contests):
    # dp 테이블 초기화: 0으로 채워진 (T+1) 크기의 1차원 배열
    dp = [0] * (T + 1)

    # 문제를 (Mi, Pi, Ri) 형태로 저장
    contests.sort(key=lambda x: x[1] * x[2])  # Pi * Ri 기준으로 정렬

    for Mi, Pi, Ri in contests:
        for t in range(T, Ri - 1, -1):
            score = t
            dp[score] = max(dp[score], dp[t - Ri] + Mi - score * Pi)

    max_score = 0
    for t in range(1, T + 1):
        max_score = max(max_score, dp[t])

    return max_score

# 입력 받기
N, T = map(int, input().split())
M = list(map(int, input().split()))
P = list(map(int, input().split()))
R = list(map(int, input().split()))

contests = [(M[i], P[i], R[i]) for i in range(N)]

# 최대 점수 출력
print(maximize_score(N, T, contests))