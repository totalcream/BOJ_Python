# 엉성한 도토리 분류기
# 2024-05-21
# 이진탐색
# 대회 당일에는 브루트포스같이 하나하나 찾아서 넣었는데
# N이 10^5이므로 시간초과가 난다.

def solve_problem():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # 첫 번째 줄: 분류기의 구멍 개수 N
    N = int(data[0])
    
    # 두 번째 줄: 각 구멍의 크기 a_1, a_2, ..., a_N
    hole_sizes = list(map(int, data[1:N+1]))
    
    # 세 번째 줄: 도토리의 개수 Q
    Q = int(data[N+1])
    
    # 네 번째 줄: 각 도토리의 크기 s_1, s_2, ..., s_Q
    acorn_sizes = list(map(int, data[N+2:N+2+Q]))

    results = []
    
    # 누적 감소량을 저장할 리스트
    cumulative_decrease = [0] * N
    cumulative_decrease[0] = 1  # 첫 번째 구멍에서의 감소량은 1
    
    for i in range(1, N):
        cumulative_decrease[i] = cumulative_decrease[i-1] + 1

    for acorn_size in acorn_sizes:
        left, right = 0, N - 1
        while left <= right:
            mid = (left + right) // 2
            if acorn_size - cumulative_decrease[mid] <= hole_sizes[mid]:
                right = mid - 1
            else:
                left = mid + 1
        results.append(left + 1)

    print(" ".join(map(str, results)))

# 문제 해결 함수 호출
solve_problem()


