import sys
sys.setrecursionlimit(10000)
t=int(input())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    matrix=[[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int,sys.stdin.readline().split())
        matrix[y][x]=1
            
    def dfs(x, y):
        global worms
        if x<0 or y<0 or x>=m or y>=n:
            return False
        if matrix[y][x]==1:
            matrix[y][x]=2
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
            return True
        return False
       
    worms=0
    for i in range(m):
        for j in range(n):
              if dfs(i, j) == True:
                 worms+=1

    
    print(worms)
