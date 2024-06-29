'''
visited 리스트를 안 만들면 안 되는 이유:
그걸 안 만들면 한번 방문했던 좌표를 -1처럼 엄청 작은 수로 설정해서 k보다 확실히 작아지도록 하려고 했지만..

k값을 조정하면서 몇 개의 덩어리가 나오는지를 구하는 전체 과정을 계속 반복해야 하기 때문에
처음 input 한 그래프는 계속 그 값을 유지하고 있어야 한다. 
반복할 때마다 그래프를 새로 만드는 것보다 
visited 그래프를 초기화하는 것이 100 쉬울 것 같다. 

그럼 어디에? 만들까요?

'''

from collections import deque
n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

max_h = 0
for i in range(n):
    if max(graph[i])>max_h:
        max_h = max(graph[i])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, k):
    q = deque([(x,y)])
    while q:
        (x, y) = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=n or nx<0 or ny>=n or ny<0:
                continue
            if graph[ny][nx] >k and visited[ny][nx]==0:
                q.append((nx, ny))
                visited[ny][nx] = 1

max_count = 0
for x in range(max_h+1):
    res = 0
    visited = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[j][i]>x and visited[j][i]==0:
                bfs(i,j,x)
                res+=1
    if res > max_count:
        max_count = res

print(max_count)