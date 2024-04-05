#히스토그램에서 가장 큰 직사각형

from sys import stdin
input = stdin.readline

def largest_rectangle_area(N, heights):
    stack = []
    max_area = 0

    for i in range(N):
        while stack and heights[stack[-1]] > heights[i]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, width * height)
        stack.append(i)

    while stack:
        height = heights[stack.pop()]
        width = N if not stack else N - stack[-1] - 1
        max_area = max(max_area, width * height)
    return max_area

if __name__ == "__main__":
    while 1:
        lst = list(map(int, input().split()))
        if lst[0] == 0:
            break
        print(largest_rectangle_area(lst[0], lst[1:]))
