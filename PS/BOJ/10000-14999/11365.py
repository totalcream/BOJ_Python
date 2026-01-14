#!밀비 급일
from sys import stdin
input = stdin.readline

while True:
    tmp = input().rstrip()
    if tmp == "END":
        break
    print(tmp[::-1])