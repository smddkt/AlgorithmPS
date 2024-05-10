from collections import deque


m, n, h = map(int, input().split())

space=[[] for _ in range(h)]

for j in range(h):
    for i in range(n):
        space[j].append(list(map(int, input().split())))


dx=[1, -1, 0, 0, 0, 0]
dy=[0, 0, 1, -1, 0, 0]
dz=[0, 0, 0, 0, 1, -1]

def bfs(z, y, x):
    queue=deque()
    for i in range(z):
        for j in range(y):
            for k in range(x):
                if space[i][j][k]==1:
                    queue.append((i, j, k))
    while queue:
        z, y, x =  queue.popleft()
        for i in range(6):
            nz=z+dz[i]
            nx=x+dx[i]
            ny=y+dy[i]

            if nx>=0 and ny>=0 and nz>=0 and nx<m and ny<n and nz<h and space[nz][ny][nx] == 0:
                space[nz][ny][nx]=space[z][y][x]+1
                queue.append((nz, ny, nx))
            else:
                continue


bfs(h, n, m)
fail=False
res=-1
maxlist=[]
for i in space:
    for j in i:
        for k in j:
            if k==0:
                fail=True
                break
        maxlist.append(max(j))

res=max(res, max(maxlist))

if fail==False: 
    print(res-1)
else: print(-1)
            



