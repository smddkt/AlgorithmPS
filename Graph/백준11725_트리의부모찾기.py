#루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정할 때 각 노드의 부모를 구하는 프로그램
from collections import deque
import sys

n = int(sys.stdin.readline()) #노드의 수

graph = [set() for i in range(n+1)]

#인접리스트 구현
for _ in range(n-1): # 정점이 n개이므로 간선은 n-1개 있음
    a, b = map(int, sys.stdin.readline().split())
    graph[a].add(b)
    graph[b].add(a)

visited = [0 for i in range(n+1)]

queue = deque([1])
while queue:
    x = queue.popleft()
    for node in graph[x]:
        if visited[node] == 0:
            visited[node] = x # 방문했을 때 0을 대체하게 되는 것은 부모 번호이다.
            queue.append(node)

for i in range(2, len(visited)):
    print(visited[i])