from sys import stdin
input = stdin.readline

N, S = map(str, input().split())
N = int(N)

cnt = 0
nick = []
chat = []
answer = ''
limit = 0
for i in range(N):
    A, B = map(str, input().split())
    nick.append(A)
    chat.append(B)

for i in range(N):
    if nick[i] == S:
        answer = chat[i]
        limit = i

for i in range(limit):
    if chat[i] == answer:
        cnt += 1

print(cnt)