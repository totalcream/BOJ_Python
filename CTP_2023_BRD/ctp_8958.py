N = int(input())

for i in range(N):
    lst = list(input())
    sum = 0
    mul = 1
    for j in lst:
        if j == 'O':
            sum += 1 * mul
            mul += 1
        else:
            mul = 1
    print(sum)