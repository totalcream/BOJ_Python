# from sys import stdin
# from collections import deque
# input = stdin.readline

# N = int(input())
# case = input().rstrip()

# dq = deque()
# dic = {}
# for _ in range(26):
#     dic[97+_] = 0

# result = [0] * len(case)
# cnt = 0

# def CheckPoint():
#     global cnt
#     print(len(dq))
#     if cnt > len(case):
#         return
#     if len(dq) < N and ord(case[cnt]) in dic:
#         dq.append(ord(case[cnt]))
#         dic[ord(case[cnt])] += 1
#         print(dic[ord(case[cnt])])
#         cnt += 1
#         CheckPoint()
#     elif len(dq) > N:
#         for _ in range(N):
#             result[cnt] = dic[ord(dq.popleft())]
#             print(dic[ord(dq.popleft())])
#         cnt += 1
#         CheckPoint()

# CheckPoint()
# print(max(result))

import sys
from collections import deque

if __name__ == '__main__':
    N = int(input())
    S = list(map(str, sys.stdin.readline().rstrip()))
    check = [0] * 26 # 알파벳 개수 세기
    size = len(S)
    left, right = 0, 0 # 투 포인터
    ans, tmp = 0, 0 # tmp : 인식한 문자 개수
    q = deque() # 현재 인식한 문자열

    while left < size and right < size:
        while right < size:
            if tmp == N and not check[ord(S[right]) - ord('a')]: # 인식한 글자 개수가 N인데 새로운 글자가 나타나면 break
                break
            if not check[ord(S[right]) - ord('a')]: # 인식한 글자 개수가 N개 이하일 때 새로운 글자 나타나면
                tmp += 1 # 인식한 문자 개수 증가
            check[ord(S[right]) - ord('a')] += 1 # 알파벳 개수 증가
            q.append(S[right])
            right += 1 # right 증가

        ans = max(ans, len(q))
        # 첫 문자 없애주기
        first = q[0]
        check[ord(first) - ord('a')] -= 1 # 첫 문자 알파벳 개수 감소
        q.popleft()
        if not check[ord(first) - ord('a')]: # 첫 문자 알파벳 개수가 0이면
            tmp -= 1 # 인식한 문자 개수 감소
        left += 1 # left 증가
    print(ans)