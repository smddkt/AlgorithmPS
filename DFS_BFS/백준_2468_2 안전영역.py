from collections import deque
n = int(input())

graph =[]

for _ in range(n):
    graph.append(list(map(int, input().split())))

max_h = 0
for i in range(n):
    if max(graph[i])>max_h:
        max_h = max(graph[i])

dx=[-1, 1, 0, 0]
dy=[0, 0, 1, -1]

def bfs(x, y, k):
    q = deque([(x, y)])
    while q:
        (x, y) = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = x+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if graph[ny][nx]>k and visited[ny][nx]==0:
                q.append((nx, ny))
                visited[ny][nx]=1

max_count = 0
for x in range(max_h+1):
    res = 0
    visited = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[j][i]>x and visited[j][i]==0:
                bfs(i, j, x)
                res+=1
    if res > max_count:
        max_count = res

print(max_count)

