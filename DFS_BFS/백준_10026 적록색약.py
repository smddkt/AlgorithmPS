from collections import deque

dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

def bfs(i, j, graph, n):
    queue=deque()
    queue.append((i, j))
    isTrue=False
    while queue:
        x, y = queue.popleft()
        if graph[x][y]!=1:
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx<0 or ny<0 or nx>=n or ny>=n:
                    continue
                elif graph[nx][ny] == graph[x][y]:
                    queue.append((nx, ny))
            graph[x][y]=1
            isTrue=True
    return isTrue


n = int(input())
graph3=[]
graph2=[]
count3=0
count2=0

for i in range(n):
    graph3.append(list(input()))
    graph2.append(graph3[i].copy())

for i in range(n):
    for j in  range(n):
        if graph2[i][j]=="R":
            graph2[i][j]="G"


for i in range(n):
    for j in range(n):
        if bfs(i, j, graph3, n)==True:
            count3+=1
        if bfs(i, j, graph2, n)==True:
            count2+=1

print(count3, count2)



'''
적록색약인 사람에게는 R=G, B 이렇게 보이고 아닌 사람에게는 R, G, B이렇게 보인다. 
처음에 DFS라고 생각했으나 방문할 위치를 stack이 아닌 queue로 쌓고 싶어서 BFS로 변경했다. 
그래프를 두 개 썼는데 복사하는 데 시행착오를 겪음... 그냥 graph1=graph2 이러면 절대 안 된다~~!
그리고 원래 같은 그래프 두 개를 BFS로 적록색약용BFS, 적록색약아닌사람용 BFS에 따로 넣으려고 했는데 적록색약용 BFS에서 자꾸 오류가 발생했다.
그래서 그래프를 적록색약용 R==G인 그래프와 일반 그래프로 나누고, BFS 함수는 적록색약 아닌 사람용 함수로 통일햇다.
'''
        
            

