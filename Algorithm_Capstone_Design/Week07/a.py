T = input()
P = input()

# # KMP전 전처리 함수
# def KMP_table(arr):
#     l = len(arr)
#     tb = [0 for _ in range(l)]

#     # 테이블 값을 불러오거나 갱신 & 패턴의 인덱스 접근(접두사)
#     pidx = 0
#     # 패턴의 인덱스 접근(접미사)
#     for i in range(1, l):
#         # pidxrk 0이 되거나, pidx번 째 글자와 i번 째 글자가 같아질때까지
#         while pidx > 0 and arr[i] != arr[pidx]:
#             pidx = tb[pidx - 1]
        
#         # 값이 일치하는 경우, pidx 1증가시키고 그 값을 tb에 저장
#         if arr[i] == arr[pidx]:
#             pidx += 1
#             tb[i] = pidx
#     # print(tb)
#     return tb

# def KMP(word, pattern):
#     # 전처리 된 테이블 불러오기
#     table = KMP_table(pattern)

#     # 결과 문자열
#     res = []
#     pidx = 0
#     l_pattern = len(pattern)
#     l_word = len(word)

#     for i in range(l_word):
#         # 단어와 패턴이 일치하지 않는 경우, pidx를 table을 활용해 변경
#         while pidx > 0 and word[i] != pattern[pidx]:
#             pidx = table[pidx - 1]
#         # 해당 인덱스에서 값이 일치한다면, pidx를 1 증가시킴
#         # 만약 pidx가 패턴의 끝까지 도달하였다면, 시작 인덱스 값을 계산하여
#         # 추가 후 pidx 값 table의 인덱스에 접근하여 변경
#         if word[i] == pattern[pidx]:
#             if pidx == l_pattern - 1:
#                 res.append(i - l_pattern + 1)
#                 pidx = table[pidx]
#             else:
#                 pidx += 1
#     return res

def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    lps = [0] * M
    global cnt
    rst = []

    computeLPS(pat, lps)
    i = 0
    j = 0
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        elif pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        
        if j == M:
            cnt += 1
            rst.append((i - j + 1))
            # print("index" + str(i - j))
            j =lps[j - 1]
    return rst


def computeLPS(pat, lps):
    leng = 0

    i = 1
    while i < len(pat):
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1

        else:
            if leng != 0:
                leng = lps[leng - 1]
            else:
                lps[i] = 0
                i += 1

cnt = 0
ans = KMPSearch(P, T)
print(cnt)
print(*ans)