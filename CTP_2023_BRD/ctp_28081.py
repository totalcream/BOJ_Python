from sys import stdin
input = stdin.readline

W, H, K = map(int, input().split())

y = []
x = []
N = int(input())
y = list(map(int, input().split()))
M = int(input())
x = list(map(int, input().split()))

board = [[0] * H] * W


print(x, y, *board)