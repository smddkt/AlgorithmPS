import sys

input= sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(y, x):
    if x>=0 and y>=0 and x<w and y<h and graph[y][x]==1:
        graph[y][x]=0
        dfs(y+1, x+1)
        dfs(y-1, x-1)
        dfs(y-1, x+1)
        dfs(y+1, x-1)
        dfs(y+1, x)
        dfs(y-1, x)
        dfs(y, x-1)
        dfs(y, x+1)
        return True
    return False

while True: 
    count=0
    w, h = map(int, input().split())
    if w==0 and h==0:
        break
    else:
        graph=[]
        for i in range(h):
            graph.append(list(map(int, input().split())))
        
        for i in range(h):
            for j in range(w):
                if dfs(i, j)==True:
                    count+=1
        print(count)