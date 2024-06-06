import heapq
from collections import defaultdict

def kth_shortest_path(n, m, k, edges):
    graph = defaultdict(list)
    for a, b, c in edges:
        graph[a].append((b, c))
    
    # 각 노드별로 k번째 최단 거리 목록
    distances = [[float('inf')] * k for _ in range(n + 1)]
    distances[1][0] = 0  # 시작점은 1번 노드, 거리 0
    
    # 우선순위 큐: (소요시간, 현재 노드)
    pq = [(0, 1)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if distances[current_node][k-1] < current_distance:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor][k-1]:
                distances[neighbor][k-1] = distance
                distances[neighbor].sort()
                heapq.heappush(pq, (distance, neighbor))
    
    # 결과 출력
    result = []
    for i in range(1, n + 1):
        if distances[i][k-1] == float('inf'):
            result.append(-1)
        else:
            result.append(distances[i][k-1])
    
    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    K = int(data[2])
    edges = []
    index = 3
    for _ in range(M):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        edges.append((a, b, c))
        index += 3

    result = kth_shortest_path(N, M, K, edges)
    for res in result:
        print(res)

if __name__ == "__main__":
    main()