#나머지
ans = []
for i in range(10):
    ans.append(int(input())%42)

print(len(set(ans)))