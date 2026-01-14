from sys import stdin
input = stdin.readline

N, K = map(int, input().split())

ans = [0] + list(map(int, input().split()))
ls = []
def build_min_heap(lst, n):
    for i in range(n//2, 0, -1):
        heapify(lst, i, n)

def heapify(lst, k, n):
    left, right = 2*k, ((2*k) + 1)
    global cnt
    # smaller = 0
    if (right <= n):
        if (lst[left] < lst[right]):
            smaller = left
        else:
            smaller = right
    elif (left <= n):
        smaller = left        
    else:
        return
    if (lst[smaller] < lst[k]):
        lst[k], lst[smaller] = lst[smaller], lst[k]
        cnt += 1
        if cnt == K:
            print(lst[k], lst[smaller])
            print(*lst[1:])
            exit()
        heapify(lst, smaller, n)

def heap_sort(lst):
    global cnt
    build_min_heap(lst, N)
    for i in range(N, 1, -1):
        lst[1], lst[i] = lst[i], lst[1]
        cnt += 1
        if cnt == K:
            print(lst[i], lst[1])
            print(*lst[1:])
            exit()
        heapify(lst, 1, i-1)

cnt = 0
heap_sort(ans)
print(-1)