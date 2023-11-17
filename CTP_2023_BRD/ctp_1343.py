import sys
case = list(map(str, sys.stdin.readline().rstrip()))
index = 0

def Check():
    global case
    X = []
    result = []
    for i, v in enumerate(case):
        if v == 'X':
            X.append('X')
        elif v == '.':
            X.append('.')

        if i == len(case)-1:
            while True:
                if len(X) >= 4:
                    for _ in range(4):
                        X.pop()
                        result.append('A')
                elif len(X) >= 2:
                    for _ in range(2):
                        X.pop()
                        result.append('B')
                else:
                    break
        elif X[-1] == '.':
            X.pop()
            while True:
                if len(X) >= 4:
                    for _ in range(4):
                        X.pop()
                        result.append('A')
                elif len(X) >= 2:
                    for _ in range(2):
                        X.pop()
                        result.append('B')
                else:
                    result.append('.')
                    break

    print(*result, sep="")

if case.count('X') % 2 != 0:
    print('-1')

else:
    Check()