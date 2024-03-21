from sys import stdin
input = stdin.readline

N = int(input())

lst1 = []
lst2 = []

for i in range(N):
    lst1.append(list(map(int, input().split())))

for i in range(N):
    lst2.append(list(map(int, input().split())))

def rotate(m):
    temp = []
    for i in range(1, N + 1):
        temp.append([i for i in range(i)])

    for i in range(N):
        for j in range(i, N):
            temp[N - i - 1][j - i] = m[j][i]
    return temp

def judge(arr1, arr2, N):
    cnt = 0
    for i in range(N):
        for j in range(i, N):
         if(arr1[j][i] != arr2[j][i]):
             cnt += 1
    return cnt

min_val = 1e9

for i in range(3):
    min_val = min(min_val, judge(lst1, lst2, N))
    lst1 = rotate(lst1)

symmetry = []
for i in range(1, N + 1):
    symmetry.append([i for i in range(i)])

for i in range(N):
    for j in range(i + 1):
        symmetry[i][i-j] = lst1[i][j]

for i in range(3):
    min_val = min(min_val, judge(symmetry, lst2, N))
    symmetry = rotate(symmetry)

print(min_val)