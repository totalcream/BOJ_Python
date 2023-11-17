T = int(input())

for i in range(T):
    case = list(input().split())
    R = case[0]
    S = case[1]
    tmp = ''
    for j in range(len(S)):
        tmp += S[j]*int(R)
    print(tmp)