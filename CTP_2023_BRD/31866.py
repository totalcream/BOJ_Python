# 손가락 게임
# 2024-05-21

A, B = map(int, input().split())

lst = [0, 2, 5]
if A in lst:
    if B in lst:
        if A == 2 and B == 5:
            print(">")
        elif A == 0 and B == 2:
            print(">")
        elif A == 5 and B == 0:
            print(">")
        elif A == B:
            print("=")
        else:
            print("<")
    else:
        print(">")
elif B in lst:
    if A in lst:
        if A == 2 and B == 5:
            print(">")
        elif A == 0 and B == 2:
            print(">")
        elif A == 5 and B == 0:
            print(">")
        elif A == B:
            print("=")
        else:
            print("<")
    else:
        print("<")
else:
    print("=")