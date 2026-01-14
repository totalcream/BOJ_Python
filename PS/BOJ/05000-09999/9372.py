from sys import stdin
input = stdin.readline
from collections import deque

T = int(input())

def BFS(graph, start, visited):
    cnt = 0
    #큐 구현을 위해 deque사용
    dq = deque([start])
    #현재 노드를 방문 처리
    visited[start] = True
    #큐가 빌 때까지 반복
    while dq:
        #큐에서 하나의 원소를 뽑아 출력
        v = dq.popleft()
        #print(v, end=' ')
        cnt += 1
        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                dq.append(i)
                visited[i] = True
    print(cnt-1)

#인접 리스트 원소 삽입
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for i in range(N+1)]
    visited = [False] * (N+1)
    for _ in range(M):
        F, T = map(int, input().split())
        if graph[F] == []: #비었으면
            graph[F] = [T]
        else:
            graph[F].append(T)
        if graph[T] == []: #비었으면
            graph[T] = [F]
        else:
            graph[T].append(F)
    BFS(graph, 1, visited)
    #print(graph)