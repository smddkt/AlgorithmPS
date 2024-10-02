#미로

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split)) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque([(x,y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny <0 or ny >= m :
                continue #왜 break가 아닌가? 왜냐면 이게. 하나가 범위 밖이어도 다른 방향으로는 다 확인을 해야 하니까..
            elif graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
            queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0, 0))








#얼음
def dfs(x, y):
    if x <= -1 or x>=n or y<= -1 or y>=m:
        return False
    
    if graph[x][y] ==0:
        graph[x][y]=1
        dfs(x-1,  y)
        dfs(x+1, y)
        dfs(x,  y-1)
        dfs(x, y+1)
        return True
    return False

n, m = map(int, input().split())
graph=[]

for i in range(n):
    graph.append(list(map(int,input())))
        
        
result=0   
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result+=1
            
print(result)
