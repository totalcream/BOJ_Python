# 카드 게임
# 2024-04-29
# 풀이 1
# 이진탐색 후 해당 값이 있으면 index + 1 그리고 리스트에서 삭제
# 이진탐색 후 해당 값이 없으면 들어갈 자리의 index 반환
# TLE받음

'''
from sys import stdin
from bisect import bisect_left, bisect_right
input = stdin.readline

N, M, K = map(int, input().split())
m_seq = list(map(int, input().split()))
k_seq = list(map(int, input().split()))
parents = [i for i in range(M)]

m_seq.sort()

def binary_search(data, target, low, high):
    middle_idx = (high + low) // 2
    middle = data[middle_idx]

    if low > high:
        return -1
    
    if target == middle:
        return middle_idx
    elif target < middle:
        return binary_search(data, target, low, middle_idx - 1)
    elif target > middle:
        return binary_search(data, target, middle_idx + 1, high)
    
for game in k_seq:
    tmp = binary_search(m_seq, game, 0, len(m_seq) - 1)
    if tmp == -1:
        idx = tmp + 1
        print(m_seq[idx])
        del m_seq[idx]
    else:
        print(m_seq[tmp+1])
        del m_seq[tmp+1]
'''

# 풀이 2
# 이분 탐색을 진행하지만 삭제하는 코드가 아니라
# 방문 배열을 하나 만들고 루프문에서 idx++를 진행하거나
# 분리 집합을 이용해서 조금 더 빠르게 구현 할 수 있다...

from sys import stdin
from bisect import bisect_left, bisect_right
input = stdin.readline

N, M, K = map(int, input().split())
m_seq = list(map(int, input().split()))
k_seq = list(map(int, input().split()))
parents = [i for i in range(M)]

m_seq.sort()

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    if y >= M:
        return
    X = find(x)
    Y = find(y)
    parents[X] = Y

for game in k_seq:
    idx = bisect_right(m_seq, game)
    idx = find(idx)
    print(m_seq[idx])
    union(idx, idx+1)