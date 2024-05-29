from sys import stdin
from collections import deque

input = stdin.readline

#인접 리스트로 구현
N, M, V = map(int, input().split())
graph = [[]] * (N+1)
visited = [False] * (N+1)

#인접 리스트 원소 삽입
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
    
#BFS에도 사용하기 위해서 그래프랑 방문체크표 copy
graph_bfs = graph.copy()
visited_bfs = visited.copy()

#인접리스트의 원소들을 정렬
for i in graph:
    i.sort()

#재귀 방식으로 구현
def DFS(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

#BFS 메서드 정의
def BFS(graph, start, visited):
    #큐 구현을 위해 deque사용
    dq = deque([start])
    #현재 노드를 방문 처리
    visited[start] = True
    #큐가 빌 때까지 반복
    while dq:
        #큐에서 하나의 원소를 뽑아 출력
        v = dq.popleft()
        print(v, end=' ')
        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                dq.append(i)
                visited[i] = True

DFS(graph, V, visited)
print()
BFS(graph_bfs, V, visited_bfs)