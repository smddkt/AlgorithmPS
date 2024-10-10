from collections import deque

n = int(input()) #정점의 개수

#주어지는 인접 행렬
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0]*n for _ in range(n)]

def bfs(x):
    queue = deque([x])
    arr = [0 for _ in range(n)]

    while queue: 
        q = queue.popleft()

        for i in range(n):
            if arr[i] == 0 and graph[q][i] == 1:
                queue.append(i)
                arr[i] = 1
                visited[x][i] = 1

for i in range(0, n):
    bfs(i)

for i in visited:
    print(*i)
     
    

