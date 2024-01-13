# 후위 표기식
from sys import stdin
input = stdin.readline

lst = input()

# def getOpPrec(op):
#     if(op == '*' or '/'):
#         return 5
#     elif(op == '+' or '-'):
#         return 3
#     elif(op == '('):
#         return 1
#     return -1

# def whoPrecOp(op1, op2):
#     op1Prec = getOpPrec(op1)
#     op2Prec = getOpPrec(op2)

#     if(op1Prec > op2Prec):
#         return 1
#     elif(op1Prec < op2Prec):
#         return -1
#     else:
#         return 0

ans = []
op_st = []
for char in lst:
    if char.isalpha():
        ans.append(char)
    else:
        if(char == '('):
            op_st.append(char)
        elif char == '*' or char == '/':
            while op_st and (op_st[-1] == '*' or op_st[-1] == '/'):
                ans.append(op_st.pop())
            op_st.append(char)
        elif char == '+' or char == '-':
            while op_st and op_st[-1] != '(':
                ans.append(op_st.pop())
            op_st.append(char)
        # elif(char == '+' or char == '-' or char == '*' or char == '/'):
        #     while(op_st and (whoPrecOp(op_st[-1], char) >= 0)):
        #         ans.append(op_st.pop())
        #     op_st.append(char)
        elif(char == ')'):
            while op_st and op_st[-1] != '(':
                ans.append(op_st.pop())
            op_st.pop()
while op_st:
    ans.append(op_st.pop())

print(*ans, sep="")