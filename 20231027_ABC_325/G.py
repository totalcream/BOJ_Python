from sys import stdin
input = stdin.readline

lst = input()
K = int(input())

# while 1:
#     if lst in 'of':
#         print(1)
#         break


tmp = lst.find('of')
print(type(lst))
if tmp != -1:
    print(lst.find('of'))
    tmplst = lst[tmp:tmp+K+2]
    print(tmplst)
    lst.replace(tmplst, " ")

print(lst)
# print(lst)
# print(K)