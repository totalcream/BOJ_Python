# 피하자
# 2024-04-30
# 홀수와 짝수의 차이가 1이라는 뜻은 홀수나 짝수가 한쪽으로
# 치우쳐 져야한다는 뜻 그래서 왼쪽으로 홀수랑 짝수를 밀고
# 홀수면 이동횟수는 만난 짝수의 수이다

N = int(input())

seq = list(map(int, input().split()))

cnt = [0, 0]
if N == 1 or N == 2:
    print(0)
    exit()

ishol = 0
isjjak = 0
for i in range(len(seq)):
    if seq[i] % 2 == 0:
        cnt[0] += ishol
    else:
        ishol += 1

for i in range(len(seq)):
    if seq[i] % 2 == 1:
        cnt[1] += isjjak
    else:
        isjjak += 1

print(min(cnt[0], cnt[1]))