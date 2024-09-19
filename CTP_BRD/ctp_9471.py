#피사노 주기
def pisano(X):
    if len(fibo) > X:
        return fibo[X]
    else:
        fibo[X] = (pisano(X-1) + pisano(X-2)) % M
        return fibo[X]

def cycle():
    X = 1
    while True:
        if fibo[X] == 0 and fibo[X-1] == 1:
            return X
        X += 1
        pisano(X)

P = int(input())

for _ in range(P):
    N, M = map(int, input().split())
    fibo = dict()
    fibo[0] = 0
    fibo[1] = 1
    fibo[2] = 1
    print(N, cycle())