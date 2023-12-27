# #조별 과제 
from sys import stdin
input = stdin.readline

def create_groups(A):
    # 학생들을 학번을 기준으로 정렬
    A.sort()
    
    # 초기값 설정
    x = 0
    y = float('inf')
    
    # 정렬된 학생들에 대해 규칙에 따라 그룹 생성
    for i in range(1, len(A), 2):
        x += A[i] - A[i - 1]
        y = min(y, x) + A[i + 1] - A[i] if i + 1 < len(A) else y
    
    return y

# 예시
N = int(input())
students = list(map(int, input().split()))
students.sort()
result = create_groups(students)
print(result)