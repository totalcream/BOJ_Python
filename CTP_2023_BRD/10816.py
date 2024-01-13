# 숫자 카드2
from sys import stdin
input = stdin.readline

N = int(input())

li_N = [*map(int, input().split())]

my_dict = {}
for i in li_N:
    if i in my_dict:
        my_dict[i] = my_dict[i] + 1
    else:
        my_dict[i] = 1

M = int(input())
li_M = [*map(int, input().split())]
for i in li_M:
    if i in my_dict:
        print(my_dict[i], end=" ")
    else:
        print(0, end=" ")