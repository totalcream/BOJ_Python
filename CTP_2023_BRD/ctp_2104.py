# 부분배열 고르기
# 히스토그램과 비슷하다고 생각
# 분할정복으로 풀이

from sys import stdin
input = stdin.readline

# N = int(input())

# lst = list(map(int, input().split()))

# def solve(s, e):
#     if s == e:
#         return lst[s] * lst[e]
#     mid = (s+e) // 2
#     ret = max(solve(s, mid), solve(mid + 1, e))

#     left = mid
#     right = mid+1

#     Sum = lst[left] + lst[right]
#     min_val = min(lst[left], lst[right])
#     ret = max(ret, min_val * Sum)
#     while left > s or right < e:
#         if right < e and (left == s or lst[left - 1] < lst[right + 1]):
#             right += 1
#             Sum += lst[right]
#             min_val = min(min_val, lst[right])
#         else:
#             left -= 1
#             Sum += lst[left]
#             min_val = min(min_val, lst[left])
#         ret = max(ret, min_val * Sum)
#     return ret

# print(solve(0, N - 1))

def max_subarray(lst, start, end):
    # 기저 사례: 배열의 길이가 1인 경우
    if start == end:
        return lst[start] * lst[end]

    # 중간 지점 계산
    mid = (start + end) // 2
    ret = max(max_subarray(lst, start, mid), max_subarray(lst, mid + 1, end))

    left = mid
    right = mid + 1

    sub_sum = lst[left] + lst[right]
    min_value = min(lst[left], lst[right])
    ret = max(ret, min_value * sub_sum)

    while left > start or right < end:
        if right < end and (left == start or lst[left - 1] < lst[right + 1]):
            right += 1
            sub_sum += lst[right]
            min_value = min(min_value, lst[right])
        else:
            left -= 1
            sub_sum += lst[left]
            min_value = min(min_value, lst[left])
        ret = max(ret, min_value * sub_sum)
    return ret

if __name__ == "__main__":
    N = int(input())
    lst = list(map(int, input().split()))

    # 최대 부분 배열의 합 계산
    result = max_subarray(lst, 0, N - 1)
    print(result)
