progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

import math
from collections import deque

def solution(progresses, speeds):

    days=deque([[] for _  in range(len(progresses))])
    count=1
    res=[]
    for i in range(len(days)):
        days[i] = math.ceil((100-progresses[i])/speeds[i]) #days 배열에 각 기능 개발에 걸리는 일수를 저장
    while days:
        count=1
        current = days.popleft()
        while days and days[0]<=current:
            count+=1
            del days[0]
        res.append(count)
   
    return res

print(solution(progresses, speeds))


"""
1.
현재 days의 0번째 원소를 popleft()로 빼내서 변수 current에 넣는다.

days[0]의 값이 며칠이든, 그 기능을 배포할 수 있는 일수까지 jump하게 해주는 과정이라고 이해하면 될 것 같다. 

이렇게 하면 적어도 한 개의 기능, 즉 days[0]만큼의 개발 일수가 걸리는 기능을 배포할 수 있다는 것이 보장되고,

다음 원소들을 차례대로 살펴보면서 한꺼번에 배포 가능한 기능의 개수를 셀 수 있다. 

이때 days[0]은 popleft를 통해 자동으로 배열에서 삭제되었으므로, 바로 두번째 while문을 실행한다.

 

2.
days에 적어도 하나의 원소가 있고, days의 0번째 원소가 현재 시점에서 개발이 완료되었다면 안쪽의 while문이 실행된다.

현재의 current 값보다 큰 값이 나오기 전까지 그 시점에서의 days[0]을 지워가고,

current보다 큰 값이 days의 0번째 원소가 되면 배포를 해야 할 시점으로 본다.

이때 count 값을 res라는 결과 리스트에 append한다.


3.
새로운 배포를 하기 위해서, 바깥쪽 while문으로 돌아가서 현재 days의 0번째 원소의 값을 current에 다시 입력한다. 이 반복문은 days에 원소가 하나도 남지 않으면(==모든 기능이 배포되면) 종료된다.
"""

