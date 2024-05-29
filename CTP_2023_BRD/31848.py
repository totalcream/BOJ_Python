# 엉성한 도토리 분류기
# 2024-05-21
# 이진탐색
# 대회 당일에는 브루트포스같이 하나하나 찾아서 넣었는데
# N이 10^5이므로 시간초과가 난다.

def process_acorns(N, slot_sizes, Q, acorn_sizes):
    # DP 배열 생성
    dp = [0] * (N + 1)
    
    # DP 배열 초기화: 각 위치에서 도토리가 빠질 수 있는 최소 크기를 계산
    for i in range(N):
        dp[i + 1] = slot_sizes[i] - i

    results = []
    
    # 각 도토리에 대해
    for acorn in acorn_sizes:
        left, right = 1, N
        while left <= right:
            mid = (left + right) // 2
            if acorn <= dp[mid]:
                right = mid - 1
            else:
                left = mid + 1
        results.append(left if left <= N else N + 1)
    
    return results

# 입력 값 읽기
N = int(input().strip())
slot_sizes = list(map(int, input().strip().split()))
Q = int(input().strip())
acorn_sizes = list(map(int, input().strip().split()))

# 도토리 처리
results = process_acorns(N, slot_sizes, Q, acorn_sizes)

# 결과 출력
print(" ".join(map(str, results)))








