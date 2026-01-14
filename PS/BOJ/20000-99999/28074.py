from sys import stdin
input = stdin.readline

lst = input()

MOBIS = [False] * 5
mobi = ['M', 'O', 'B', 'I', 'S']

mobidic = dict(zip(mobi, MOBIS))
ans = []
for i in lst:
    if i in mobi:
        if mobidic[i] == True:
            pass
        else:
            mobidic[i] = True
            ans.append(True)

if len(ans) >= 5:
    print('YES')
else:
    print('NO')
