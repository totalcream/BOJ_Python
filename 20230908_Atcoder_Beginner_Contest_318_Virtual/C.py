from sys import stdin
input = stdin.readline

N, D, P = map(int, input().split())
Fyen = list(map(int, input().split()))

print(Fyen)
#1일 여행에 걸리는 금액은 Fyen[N]
#1일 주유패스는 D장 세트로 P엔에 판매
#구입한 패스는 1매당 사용가능, 남아있어도 상관x
#N일일 여행에 소요되는 총 금액, 

