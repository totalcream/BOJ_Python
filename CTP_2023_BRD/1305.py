# 광고
# 2024-04-18
# KMP알고리즘의 실패함수를 사용해서 구하기

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
    return lps

L = int(input())
pat = input().rstrip()

lst = [0] * L
ans = computeLPS(pat, lst)
#print(ans)
print(L - ans[-1])