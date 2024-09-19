from sys import stdin
input = stdin.readline

N = int(input())
lst = []
for i in range(N):
    tmp = int(input())
    lst.append(tmp)

lst.sort()

print(*lst, sep="\n")
