# 간단한 순열 문제
# 2024-05-24
# 애드훅, 스택, 자료 구조

def count_valid_pairs(N, P):
    count = 0
    
    # Iterate over all possible (i, j) pairs
    for i in range(N - 1):
        max_between = 0
        for j in range(i + 1, N):
            max_between = max(max_between, P[j - 1])
            if min(P[i], P[j]) > max_between:
                count += 1
                
    return count

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    P = list(map(int, data[1:]))
    
    result = count_valid_pairs(N, P)
    print(result)

if __name__ == "__main__":
    main()
