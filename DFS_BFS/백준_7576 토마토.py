from collections import deque

def bfs(m, n):
    queue=deque()
    '''
    익은 토마토가 한 개보다 많을 수 있으므로
    bfs함수 이전에 이미 익어 있는 토마토의 위치를 모두 큐에 넣음. 
    '''
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                queue.append((i, j))

    while(queue):
        x, y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==1:
                continue
            if graph[nx][ny]==-1:
                continue
            if graph[nx][ny]==0:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx, ny))

m, n = map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))

dx=[-1, 1, 0, 0]
dy=[0, 0, 1, -1]


bfs(m, n)

fail = False
res = -1

for i in graph:
    for j in i:
        if j == 0:
            fail=True
    res=max(res, max(i))

if fail: 
    print(-1)
else: print(res-1)

'''

m,n 입력 순서가 헷갈린다.

bfs 함수에서 리턴값을 받는 방식이 아니라 
함수 정의 --> 함수 한번 실행해서 그래프의 값들 업데이트 --> 따로 출력 조건 설정해서 출력
하는 게 어려웠다. 

'''