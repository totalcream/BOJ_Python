import functools
import sys

sys.setrecursionlimit(50000)

@functools.cache
def fibo(X):
    if X == 1 or X == 2:
        return 1
    return fibo(X - 1) + fibo(X - 2)

fibo(10000000)


# dict = {}
# dict[0] = 1
# @functools.cache
# def sy(N):
#     if N in dict:
#         return dict[N]
#     else:
#         dict[N] = (sy((N//P-X)) + sy((N//Q-Y)))
#         return dict[N]

# #lst = list(map(int, input().split()))
# N, P, Q, X, Y = map(int, input().split())
# #print(N, P, Q, X, Y)
# #print(lst[4])
# print(sy(N))
# import functools

# dp = [0] * 100
# @functools.cache
# def fibo(X):
#     if X == 1 or X == 2:
#         return 1
    
#     if dp[X] != 0:
#         return dp[X]
    
#     dp[X] = fibo(X - 1) + fibo(X - 2)
#     return dp[X]

# print(fibo(99))

# N = int(input())

# dp = [0] * 30001

# for i in range(2, N + 1):
#     dp[i] = dp[i - 1] + 1

#     if i % 2 == 0:
#         dp[i] = min(dp[i], dp[i // 2] + 1)

#     if i % 3 == 0:
#         dp[i] = min(dp[i], dp[i // 3] + 1)

#     if i % 5 == 0:
#         dp[i] = min(dp[i], dp[i // 5] + 1)
    
#     print('f(' + str(i) + ')', end='')

# print(dp[N])