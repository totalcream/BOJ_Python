# 트리의 순회

from sys import stdin, setrecursionlimit
input = stdin.readline

setrecursionlimit(10**6)

N = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

nodenum = [0] * (N + 1)

for i in range(N):
    nodenum[inorder[i]] = i

def preorder(inStart, inEnd, postStart, postEnd):
    if (inStart > inEnd) or (postStart > postEnd):
        return
    
    root = postorder[postEnd]

    leftNode = nodenum[root] - inStart
    rightNode = inEnd - nodenum[root]

    print(root, end=' ')
    preorder(inStart, inStart + leftNode - 1, postStart, postStart + leftNode - 1)
    preorder(inEnd - rightNode + 1, inEnd, postEnd - rightNode, postEnd - 1)

preorder(0, N -1, 0, N -1)