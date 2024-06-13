def solution(n, edge):
    graph = [[]for _ in range(n+1)]
    not_visited = [i for i in range(2, n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    

    far = {1}
    while not_visited:
        farther = set()
        for node in far:
            for j in graph[node]:
                if j in not_visited:
                    not_visited.remove(j)
                    farther.add(j)
        if not farther:
            return 1
        far = farther
    return len(far)


#bfs 풀이 추가 : 시간복잡도 줄인 풀이
from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    dist = [0]*(n+1)
    for i, j in edge:
        graph[i].append(j)
        graph[j].append(i)
    
    queue = deque([1])
    while queue:
        x = queue.popleft()
        if graph[x]:
            for k in graph[x]:
                if k == 1:
                    continue
                if dist[k] == 0:
                    dist[k] = dist[x]+1
                    queue.append(k)
    
    a = max(dist)
    answer = dist.count(a)
    
    return answer