# 최소 스패닝 트리
# 크루스칼 알고리즘 사용
# 유니온 파인드를 활용해서 O(1)에 정점 두개를 찾음
# 루트가 더 큰값을 작은 루트 값으로 연결해준다.
# 마지막으로 가중치를 더해서 비용을 계산한다.


V, E = map(int, input().split())
edges = []

for _ in range(E):
    edges.append(list(map(int, input().split())))

root = dict()
for i in range(1, V+1):
    root[i] = i

def find(x):
    if root[x] == x:
        return x
    else:
        root[x] = find(root[x])
        return root[x]


def union(x, y):
    x = find(x)
    y = find(y)

    root[y] = x


edges = sorted(edges, key=lambda x: x[2])

total_cost = 0

for edge in edges:
    if find(edge[0]) == find(edge[1]):
        continue
    else:
        total_cost += edge[2]
        union(edge[0], edge[1])

print(total_cost)