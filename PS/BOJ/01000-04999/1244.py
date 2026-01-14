# 스위치 켜고 끄기
# 2025-10-15
# 구현

from sys import stdin
input = stdin.readline

N = int(input())
switches = list(map(int, input().split()))
M = int(input())

for _ in range(M):
    gender, pos = map(int, input().split())
    # 남학생
    if gender == 1:
        for i in range(pos-1, N, pos):
            if switches[i] == 0:
                switches[i] = 1
            else:
                switches[i] = 0
    # 여학생
    else:
        # 우선 일단 대칭부터 바꾸기
        left = pos - 2
        right = pos
        if switches[pos-1] == 0:
            switches[pos-1] = 1
        else:
            switches[pos-1] = 0
        # 대칭이면서 같을 때까지 반복
        while left >= 0 and right < N:
            if switches[left] == switches[right]:
                if switches[left] == 0:
                    switches[left] = 1
                    switches[right] = 1
                else:
                    switches[left] = 0
                    switches[right] = 0
                left -= 1
                right += 1
            else:
                break

for i in range(N):
    print(switches[i], end=' ')
    # 20개씩 끊어서 출력
    if (i+1) % 20 == 0:
        print()