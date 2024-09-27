import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())
graph=[[] for _ in  range(n+1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
  

connected=[]

def dfs(x):
    if x not in connected:
        connected.append(x)
        for j in graph[x]:
            dfs(j)
        return True
    return False
    
count=0              
for k in range(1, n+1):
    if dfs(k)==True:
        count+=1
        
print(count)
            