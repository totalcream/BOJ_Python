lst = list(map(list, input().split()))

lst[0].reverse()
lst[1].reverse()

if "".join(lst[0]) > "".join(lst[1]):
    print("".join(lst[0]))
else:
    print("".join(lst[1]))

#삼항 연산자 표현식 코드
#print("".join(lst[0])) if "".join(lst[0]) > "".join(lst[1]) else print("".join(lst[1]))