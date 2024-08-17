import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
roads=[[] for i in range(n+1)]

for i in range(1, m+1):
    a, b = map(int, input().split())
    roads[a].append(b)

from collections import deque

dist=[0]*(n+1)
visited=[-1]*(n+1)
empty=True

def bfs(x): 
    visited[x]=1
    queue=deque([x])

    while queue: 
        now= queue.popleft()
        for j in roads[now]:
            if visited[j]==-1:
                visited[j]=1
                queue.append(j)
                dist[j]=dist[now]+1

    return dist
        
bfs(x)


for i in range(len(dist)):
    if dist[i]==k:
        empty=False
        print(i)

if empty==True:
    print(-1)
