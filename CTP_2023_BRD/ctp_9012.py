from sys import stdin
input = stdin.readline

N = int(input())

for i in range(N):
    st = []
    s = input()
    isVPS = True

    for ch in s:
        if ch == '(':
            st.append(('('))
        if ch == ')':
            if st:
                st.pop()
            elif not st:
                isVPS = False
                break
    if not st and isVPS:
        print('YES')
    elif st or not isVPS:
        print('NO')