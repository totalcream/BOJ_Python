code = list(map(int, input().split()))

if code == sorted(code):
    print('ascending')
elif code == sorted(code, reverse=True):
    print('descending')
else:
    print('mixed')