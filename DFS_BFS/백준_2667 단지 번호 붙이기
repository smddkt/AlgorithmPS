def dfs(x, y):
    global count
    if x<0 or y<0 or x>=MapSize or y>=MapSize:
        return False

    if graph[x][y]==1:
        graph[x][y]=2
        count+=1
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False     
    
MapSize = int(input())
graph=[]
countarr=[]
count=0 

for i in range(MapSize):
    graph.append(list(map(int,input())))

Complex=0
for i in range(MapSize):
    for j in range(MapSize):
        if dfs(i,j)==True:
            Complex+=1
            countarr.append(count)
            count=0



print(Complex)
for i in sorted(countarr):
    print(i)
