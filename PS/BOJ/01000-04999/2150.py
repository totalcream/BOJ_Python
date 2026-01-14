# 2150 SCC
# 구현은 타잔 알고리즘
# 코사라주도 구현해 봐야함
from sys import stdin, setrecursionlimit
input = stdin.readline

setrecursionlimit(10**6)

def SCC(G, V):
    finished = [False] * (V + 1)
    # 누적 라벨: 노드를 한 번 방문 할 때마다 1씩 증가
    label = [0]
    # 고유 라벨 번호 저장
    labels = [0] * (V + 1)
    ans, s = [], []

    def _SCC(U):
        label[0] += 1
        # 자기 자신이 부모노드라고 가정
        parent = labels[U] = label[0]
        s.append(U)

        for v in G[U]:
            if not labels[v]:
                # 아직 방문 안함
                parent = min(parent, _SCC(v))
            elif not finished[v]:
                # 방문은 했지만 SCC처리가 아직 안된 노드 = 사이클 형성됨
                parent = min(parent, labels[v])
        
        if parent == labels[U]:
            # 자기 자신이 사이클 중 가장 먼저 탐색되는 경우
            # == 루트 노드임
            scc_set = []
            while s:
                p = s.pop()
                scc_set.append(p)
                finished[p] = True
                if U == p:
                    break
            ans.append(scc_set)
        return parent
    for e in range(1, V + 1):
        if not labels[e]:
            _SCC(e)
    return ans


V, E = map(int, input().split())
G = [list() for _ in range(V + 1)]

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)

ans = SCC(G, V)

for e in ans:
    e.sort()
ans.sort(key=lambda e: e[0])

print(len(ans))
for e in ans:
    res = ''
    for _e in e:
        res += str(_e) + ' '
    res += '-1'
    print(res)