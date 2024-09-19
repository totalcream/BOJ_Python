#주사위

from sys import stdin
input = stdin.readline

from itertools import combinations, permutations, product

# nums = [1, 2, 3, 4]
# combi = list(combinations(nums, 2))
# perm = list(permutations(nums, 2))

S1, S2, S3 = map(int, input().split())
lstS1 = []
for i in range(S1):
    lstS1.append(i+1)

lstS2 = []
for i in range(S2):
    lstS2.append(i+1)

lstS3 = []
for i in range(S3):
    lstS3.append(i+1)

lst = []
lst.append(lstS1)
lst.append(lstS2)
lst.append(lstS3)

combi = list(product(*lst))
res = 0
sumlst = [0]*80
for i in combi:
    sumlst[sum(i)-1] += 1
    res = max(sumlst)
    
print(sumlst.index(res)+1)