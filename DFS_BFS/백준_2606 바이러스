computers = int(input())  # 전체 컴퓨터의 수
n = int(input())   #직접 연결되어 있는 컴퓨터 쌍의 수 


#인접리스트로 만들기!
list=[[] for _ in range(computers+1)]
 #이차원 리스트 초기화

for i in range(n):
    a, b = map(int, input().split())
    list[a].append(b)
    list[b].append(a)
    
    #각각의 노드에 연결된 노드들의 정보를 기록


#dfs 함수
connected=[] #1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터들을 추가할 곳

def dfs(x):
    global connected
    for i in list[x]:
        if i!=1 and i not in connected:
            connected.append(i)
            dfs(i)
    return len(connected)


print(dfs(1))



    
