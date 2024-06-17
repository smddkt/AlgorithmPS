'''
신장트리: 최소 간선으로 그래프의 모든 정점이 연결되는 그래프.
계속 회전하면서 연결되는 게 아니기 때문에, 신장 그래프가 아닌 신장 트리이다.
간선의 개수는 정점의 개수-1이다. 

최소 신장트리: 가중치 그래프에서 만들 수 있는 신장 트리 중 합계가 최소인 것. 
프림, 크루스칼 알고리즘 등으로 구현한다.
'''

G1 = None
nameAry = ['춘천', '서울', '속초', '대전', '광주', '부산']
춘천, 서울, 속초, 대전, 광주, 부산 = 0, 1, 2, 3, 4, 5

edgeAry = []
for i in range(gSize) :
    for k in range(gSize) :
        if G1.graph[i][k] != 0 :
            edgeAry.append([G1.graph[i][k], i, k])

# 간선 정렬 : 가중치를 기준으로 내림차선으로 간선을 정렬한다. itemgetter(위치) 는 위치에 해당하는 값을 선택해서 정렬함.
from operator import itemgetter
edgeAry = sorted(edgeAry, key=itemgetter(0), reverse= True)

#중복 간선 제거 : 동일한 간선 ex)서울광주, 광주서울 이 두 개씩 배치되었으므로 0번째부터 2번째, 4번째만 추출하여 가중치 높은 순서대로, 중복제거된 배열만들자. 
newAry = []
for i in range(0, len(edgeAry), 2):
    newAry.append(edgeAry[i])

#가중치가 높은 간선부터 제거. 모든 도시가 서로 연결되어 있도록 하는 선에서만, 최소신장트리 간선개수(정점-1개)가 될 때까지

#서울-광주 간선은 가장 가중치가 높고, 제거해도 동떨어진 정점이 생기지 않는다. 
index = 0
 
start = newAry[index][1] # 서울
end = newAry[index][2] #광주

G1.graph[start][end] = 0 
G1.graph[end][start] = 0

del(newAry[index])

#두 번째로 가중치가 높은 서울-속초 간선! 제거해도 동떨어진 점이 없다. 
index = 0

start = newAry[index][1]
end = newAry[index][2]

G1.graph[start][end] = 0
G1.graph[end][start] = 0 

del(newAry[index])

#세 번째로 가중치가 높은 대전-부산 간선 역시 제거해도 동떨어진 정점이 생기지 않는다. 

index = 0

start = newAry[index][1]
end = newAry[index][2]

G1.graph[start][end] = 0
G1.graph[start][end] = 0

del(newAry[index])

# 다음으로 가중치가 높은 광주-부산 간선을 제거하면 부산 정점은 동떨어진 점이 된다. 제거했다가 취소하고 index +1 해서 다음으로 가중치가 높은 간선을 제거해 보자.
index = 0

start = newAry[index][1]
end = newAry[index][2]
saveCost = newAry[index][0] #복구할 것을 대비해서 가중치 기억하기

G1.graph[start][end] = 0
G1.graph[end][start] = 0

startYN = findVertex(G1, start)
endYN = findVertex(G1, end)

if startYN and endYN : # 두 정점이 모두 그래프와 연결되어 있다면? end라는 게 뭐임? end는 부산인데 연결이 안 되어 있을 것. 
    del(newAry[index])
else: 
    G1.graph[start][end]= saveCost
    G1.graph[end][start]= saveCost
    index += 1 #다음으로 가중치가 높은 걸 찾으러 넘어가는 거임 다 복구 해놓고


#자 대전 광주 간선 차례인데 이것도 제거하면 뭐가 연결이 안 됨. 삭제했다가 if문에 걸려서 복구 되었다고 치고 가중치만 하나 더 올리겠음. 
index+=1

#다음으로 가중치가 높은 춘천 속초 간선은 제거해도 동떨어진 접점이 없음 + 이거 제거하면 최소 신장트리의 간선 개수가 되므로 최소신장트리가 완성됨.