# 알람 시계

H, M = map(int, input().split())

if 45 < M <= 59:
    print(f"{H} {M-45}")

elif 0 <= M < 45:
    if H >= 1:
        print(f"{H - 1} {(60 + M) - 45}")
    else:
        print(f"{23} {(60 + M) - 45}")

else:
    print(f"{H} {0}")