from sys import stdin
input = stdin.readline

H, W = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(H)]

arr = list(zip(*lst))

for i in arr:
    print(*i)