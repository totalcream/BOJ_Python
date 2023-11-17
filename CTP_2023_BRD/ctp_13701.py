#중복 제거
from sys import *
import os
input = stdin.readline

# numbers = list(map(int, input().split()))

# ans = [False] * 2**25
# check = 0b0000000000000000000000000
# for i in numbers:
#     if check & (1 << i) != 0:
#         pass
#     else:
#         check |= (1 << i)
#         print(check, end=" ")

def read_word():

    unstdin = os.fdopen(stdin.fileno(), 'rb', buffering=1000000)
    ch = unstdin.read(1)
    while True:
        num = 0
        while not (ch == b'\n' or ch == b'' or (ch >= b'0' and ch <= b'9')):
            ch = unstdin.read(1)
        if ch == b'\n' or ch == b'':
            break
        while ch >= b'0' and ch <= b'9':
            num = num * 10 + int(ch)
            ch = unstdin.read(1)
        yield num

def set_bit(n):
    nn = n // 8
    nr = n % 8

    ret = (bits[nn] & (1 << nr)) == 0

    bits[nn] |= (1 << nr)

    return ret

if __name__ == '__main__':
    bits = bytearray(4194304)

    try:
        sys.stdin = open("13701_input.txt")
    except FileNotFoundError:
        pass

    for num in read_word():
        if set_bit(num) == True:
            print(num, end=" ")
    print()