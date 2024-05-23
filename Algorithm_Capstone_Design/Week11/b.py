def printOptimalParens(s, i, j):
    if i == j:
        print(f"M{i + 1}", end='')
    else:
        print("(", end='')
        printOptimalParens(s, i, s[i][j])
        print("*", end='')
        printOptimalParens(s, s[i][j] + 1, j)
        print(")", end='')


def matrixChainOrder(p, n):
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    print(m[0][n - 1])
    printOptimalParens(s, 0, n - 1)


N = int(input())

p = []
for _ in range(N):
    rows, cols = map(int, input().split())
    p.append(rows)
    if _ == N - 1:
        p.append(cols)

matrixChainOrder(p, N)
