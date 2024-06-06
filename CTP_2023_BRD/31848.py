# 엉성한 도토리 분류기
# 2024-05-21
# 이진탐색
# 대회 당일에는 브루트포스같이 하나하나 찾아서 넣었는데
# N이 10^5이므로 시간초과가 난다.

def solve(N, holes, M, dotoris):
    Where = [0] * (N + 1)
    fin = 0

    for i in range(1, N + 1):
        if holes[i][0] <= fin:
            continue
        if Where[N] != 0:
            break
        for j in range(fin, min(holes[i][0], N) + 1):
            if Where[j] == 0:
                Where[j] = holes[i][1]
        fin = holes[i][0]

    result = [Where[dotoris[i]] for i in range(1, M + 1)]
    print(" ".join(map(str, result)))

def main():
    import sys
    input = sys.stdin.read
    input_data = input().split()
    
    idx = 0

    N = int(input_data[idx])
    idx += 1

    holes = [None] * (N + 1)
    for i in range(1, N + 1):
        hole_first = int(input_data[idx])
        idx += 1
        holes[i] = (hole_first + (i - 1), i)

    M = int(input_data[idx])
    idx += 1

    dotoris = [0] * (M + 1)
    for i in range(1, M + 1):
        dotoris[i] = int(input_data[idx])
        idx += 1

    solve(N, holes, M, dotoris)

if __name__ == "__main__":
    main()

# 아래는 이분탐색 풀이법
# import sys
# from bisect import *  # bisect 모듈을 임포트하여 이분 탐색 함수들을 사용

# def input(): return sys.stdin.readline().strip()  # 입력을 읽기 위한 함수 정의

# n = int(input())  # 정수 n을 입력받음 (배열의 크기)
# arr = list(map(int, input().split()))  # n개의 정수를 입력받아 리스트 arr에 저장
# q = int(input())  # 정수 q를 입력받음 (질문 수)
# brr = list(map(int, input().split()))  # q개의 정수를 입력받아 리스트 brr에 저장
# ans = [0]*q  # 결과를 저장할 리스트 ans를 q의 크기로 초기화
# can = [0]  # can 리스트를 초기화, can[i]는 i번째 요소까지 최대 값을 저장

# # arr 배열을 순회하며 can 리스트를 채움
# for i in range(n):
#     can.append(max(can[i], arr[i] + i))  # 현재 인덱스까지의 최대값을 can에 추가

# # 질문 리스트 brr을 순회하며 각 질문에 대한 답을 계산
# for i in range(q):
#     x = brr[i]  # brr에서 현재 질문 값을 가져옴
#     ix = bisect_left(can, x)  # 이분 탐색을 사용하여 can에서 x 이상의 값을 찾음
#     ans[i] = ix  # 결과를 ans 리스트에 저장

# # 결과를 출력
# print(*ans)