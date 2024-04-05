# 히스토그램

from sys import stdin
input = stdin.readline

def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    n = len(heights)

    # 히스토그램에서 가장 큰 직사각형의 넓이를 계산
    for i in range(n):
        # 현재 인덱스를 기준으로 왼쪽에 있는 더 작은 막대를 찾음
        while stack and heights[stack[-1]] > heights[i]:
            # 막대 높이
            height = heights[stack.pop()]
            # 막대의 너비
            width = i if not stack else i - stack[-1] - 1
            # 현재까지의 최대 넓이 업데이트
            max_area = max(max_area, width * height)
        stack.append(i)

    # 스택에 남아 있는 막대들에 대해 최대 넓이 계산
    while stack:
        height = heights[stack.pop()]
        width = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, width * height)

    return max_area

if __name__ == "__main__":
    n = int(input())
    heights =[]

    for _ in range(n):
        heights.append(int(input()))
    # 최대 직사각형의 넓이 계산
    result = largest_rectangle_area(heights)
    print(result)
