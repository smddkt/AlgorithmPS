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