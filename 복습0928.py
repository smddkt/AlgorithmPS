#1012

# from collections import deque

# case = int(input())

# for _ in range(case):
#     m, n, k = map(int, input().split())
#     count = 0 
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]

#     graph = [[0]*m for i in range(n)]
#     for _ in range(k):
#         a, b = map(int, input().split())
#         graph[b][a] = 1

#     queue = deque([(m, n)])

#     while len(queue)>=1: 
#         x, y = queue.popleft()
#         canmove=0
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if nx<0 or nx>=m or ny<0 or ny>=n:
#                 continue
#             if graph[ny][nx]==1:
#                 queue.append((nx, ny))  
#                 canmove+=1  
#             #만약 네 방면 모두 0이었다면?
#             if canmove == 0:
#                 count+=1

#     print(count)



from collections import deque

case = int(input())

def bfs(m, n, k):
    count = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    graph = [[0]*m for i in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
    
    queue = deque([(0, 0)])

    while len(queue) >= 1:
        x, y = queue.popleft()
        canmove = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            
            if graph[ny][nx] == 1:
                


for _ in range(case):
    print(bfs(map(int, input().split())))