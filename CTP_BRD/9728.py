# Pair Sum
# 2024-07-07
# N개의 조합에서 M이 되는 경우의 수를 구하는 문제

def count_pairs_with_sum(arr, M):
    # 두 포인터를 사용하여 합이 M이 되는 쌍의 수를 세는 함수
    left, right = 0, len(arr) - 1
    count = 0
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == M:
            count += 1  # 합이 M이면 쌍의 수 증가
            left += 1
            right -= 1
        elif current_sum < M:
            left += 1  # 합이 M보다 작으면 왼쪽 포인터 증가
        else:
            right -= 1  # 합이 M보다 크면 오른쪽 포인터 감소
    return count

def main():
    import sys
    input = sys.stdin.read  # 표준 입력을 읽어오는 함수
    data = input().strip().split('\n')
    
    T = int(data[0])  # 테스트 케이스의 수
    index = 1
    results = []
    for case_number in range(1, T + 1):
        N, M = map(int, data[index].split())  # N과 M을 입력받음
        index += 1
        array = list(map(int, data[index].split()))  # 배열 입력받음
        index += 1
        result = count_pairs_with_sum(array, M)  # 합이 M이 되는 쌍의 수 계산
        results.append(f"Case #{case_number}: {result}")  # 결과 저장
    
    for result in results:
        print(result)  # 모든 결과 출력

if __name__ == "__main__":
    main()  # 메인 함수 실행

