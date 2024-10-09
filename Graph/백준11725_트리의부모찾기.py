#루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정할 때 각 노드의 부모를 구하는 프로그램
from collections import deque
import sys

n = int(sys.stdin.readline()) #노드의 수

graph = [set() for i in range(n+1)]

#인접리스트 구현
for _ in range(n):
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

for i in range(1, len(visited)):
    print(visited[i])





#그래프에서 0번째를 뺀다면?

from collections import deque
import sys

n = int(sys.stdin.readline()) 

graph = [set() for i in range(n)]


for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1].add(b)
    graph[b-1].add(a)

visited = [0 for i in range(n)] 

queue = deque([1])
while queue: 
    x = queue.popleft()
    for node in graph[n-1]:
        if visited[node -1] == 0:
            visited[node -1] == x 
            queue.append(node)

for i in range(1, len(visited)):
    print(visited[i])
