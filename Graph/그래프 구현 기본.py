class Graph() :
    def __init__ (self, size):
        self.size=size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]
        
G1, G3 = None, None

G1 = Graph(4)
G1.graph[0][1]=1; G1.graph[0][2]=1; G1.graph[0][3]=1
G1.graph[1][0]=1; G1.graph[1][2]=1
G1.graph[2][0]=1; G1.graph[2][1]=1; G1.graph[2][3]=1
G1.graph[3][0]=1; G1.graph[3][2]=1

print('## G1 무방향 그래프 ##')
for row in range(4):
    for col in range(4):
        print(G1.graph[row][col], end = ' ')
    print()
    
G3=Graph(4)
G3.graph[0][1]=1; G3.graph[0][2]=1
G3.graph[3][0]=1; G3.graph[3][2]=1

print('## G3 방향 그래프 ##')
for row in range(4):
    for col in range(4):
        print(G3.graph[row][col], end=' ')
    print()





#다른모양 그래프
class Graph() :
    def __init__ (self, size):
        self.size=size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]
        
G1, G3 = None, None

G1 = Graph(4)
G1.graph[0][3]=1
G1.graph[1][2]=1; G1.graph[1][3]=1
G1.graph[2][1]=1
G1.graph[3][0]=1; G1.graph[3][1]=1

print('## G1 무방향 그래프 ##')
for row in range(4):
    for col in range(4):
        print(G1.graph[row][col], end = ' ')
    print()


    
    
    
    
#이름 나오는 무방향 그래프


#클래스와 함수 선언
class Graph() :
    def __init__ (self, size):
        self.size=size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]
        
def printGraph(g):
    print('   ', end=' ')
    for v in range(g.size):
        print(nameArr[v], end = ' ')
    print()
    for row in range(g.size):
        print(nameArr[row], end = ' ')
        for col in range(g.size):
            print(g.graph[row][col], end = '    ')
        print()
    print()
    

#전역변수 선언   
G1=None
nameArr = ['문별', '솔라', '휘인', '쯔위', '선미', '화사']
문별, 솔라, 휘인, 쯔위, 선미, 화사 = 0, 1, 2, 3, 4, 5


#메인 코드
gsize = 6
G1=Graph(gsize)
G1.graph[문별][솔라]=1; G1.graph[문별][휘인]=1
G1.graph[솔라][문별]=1; G1.graph[솔라][쯔위]=1
G1.graph[휘인][문별]=1; G1.graph[휘인][쯔위]=1
G1.graph[쯔위][솔라]=1; G1.graph[쯔위][휘인]=1; G1.graph[쯔위][선미]=1; G1.graph[쯔위][화사]=1
G1.graph[선미][쯔위]=1; G1.graph[선미][화사]=1
G1.graph[화사][쯔위]=1; G1.graph[화사][선미]=1

print('## G1 무방향 그래프 ##')
printGraph(G1)



# 깊이 우선 탐색의 구현

class Graph():
    def __init__ (self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

G1= None
stack = []
visitedAry = []

G1 = Graph(4)
G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] =1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print('## G1 무방향 그래프 ##')
for row in range(4) :
    for col in range(4):
        print( G1.graph[row][col], end = ' ')
    print()


current = 0
stack.append(current)
visitedAry.append(current)

while (len(stack) !=0):
    next = None
    for vertex in range(4):
        if G1.graph[current][vertex] == 1 :
            if vertex in visitedAry:
                pass
            else:
                next = vertex 
                break

    if next != None :
        current = next
        stack.append(current)
        visitedAry.append(current)
    else :
        current = stack.pop()

print('방문 순서 -->', end = ' ')
for i in visitedAry :
    print(chr(ord('A')+i), end = ' ')
