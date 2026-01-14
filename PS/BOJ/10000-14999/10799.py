ir = input()
stk = []
cnt = 0

for i in range(len(ir)):
    if ir[i] == "(":
        stk.append("(")
    else:
        if ir[i-1] == "(":
            stk.pop()
            cnt += len(stk)

        else:
            stk.pop()
            cnt += 1

print(cnt)