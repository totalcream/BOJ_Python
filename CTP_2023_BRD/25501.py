# 재귀의 귀재

def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)

N = int(input())
cnt = 0
for i in range(N):
    case = input()
    cnt = 0
    if isPalindrome(case):
        print(f"1 {cnt}")
    else:
        print(f"0 {cnt}")