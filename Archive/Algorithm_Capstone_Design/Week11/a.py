from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10**5)
N = int(input())
dp = [[0] * N for _ in range(N)]
lst = [list(map(int, input().split())) for _ in range(N)]
dpcost = [[0] * N for _ in range(N)]

def order(p, i, j):
    if i == j:
        print(f"M{i+1}", end='')
    else:
        k = p[i][j]
        print("(", end='')
        order(p, i, k)
        print("*", end='')
        order(p, k + 1, j)
        print(")", end='')


for term in range(1, N):
    for start in range(N):
        if start + term == N:
            break
        
        dp[start][start+term] = int(1e9)

        for t in range(start, start + term):
            dp[start][start + term] = min(dp[start][start + term], dp[start][t] + dp[t + 1][start + term] + lst[start][0] * lst[t][1] * lst[start + term][1])
            dpcost[start][term] = t

print(dp[0][N - 1])
for i in dpcost:
    print(i)
#order(dpcost, 0, N - 1)
print()