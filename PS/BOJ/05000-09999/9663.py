# N-Queen
N = int(input())

ans = 0
row = [0] * N

def is_promising(X):
    for i in range(X):
        if row[X] == row[i] or abs(row[X] - row[i]) == abs(X - i):
            return False
    
    return True

def N_Queens(X):
    global ans
    if X == N:
        ans += 1
        return
    
    else:
        for i in range(N):
            row[X] = i
            if is_promising(X):
                N_Queens(X+1)

N_Queens(0)
print(ans)