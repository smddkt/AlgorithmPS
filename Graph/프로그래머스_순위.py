#플로이드 워셜 알고리즘 사용
'''
a가 b를 이기고 b가 c를 이겼다면, 
a는 c를 이긴 것이고 c는 a에게 진 것이다.

c는 a에게 진 것이다!라는 부분을 코드에 표현하지 않아서 
처음에 몇 개의 테스트케이스에서 부적확한 결과가 나왔다.
간접적인 승패의 결과를 전파할 때. 나의 풀이에서는 이김 = 1, 짐 = -1로 표현하고 
최종적으로 승패를 알 수 없는 0의 개수를 세서 답을 구했기 때문이다.


만약 다르게 풀어서 진 것은 표현하지 않기로 했다면
마지막에 1의 숫자를 셀 때 해당 인덱스를 행으로 하는 곳에서도 세고, 해당 인덱스를 열로 하는 곳에서도 세면 된다.
(열로 봤을 때 1이 추가된 것은 그 행의 인덱스를 가진 선수에게 졌기 때문임)
'''


def solution(n, results):
    graph = [[0]*(n+1)for _ in range(n+1)]
    for res in results:
        win, lose = res[0], res[1]
        graph[win][lose] = 1
        graph[lose][win] = -1

    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                if graph[i][j] == -1 and graph[j][k] == -1:
                    graph[i][k] = -1
                    graph[k][i] = 1
                elif graph[i][j] == 1 and graph[j][k] == 1:
                    graph[i][k] = 1
                    graph[k][i] = -1
                        
    answer = 0  
    
    for player in graph:
        if player.count(0)==2:
            answer+=1
        
    return answer