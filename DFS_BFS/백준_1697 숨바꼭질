n, k = map(int, input().split())
#최단 경로 찾는 건데 n은 -1, +1, *2 중에 하나 할 수 있다. 

from collections import deque

arr=[0]*(100001)

def bfs(x):

    queue=deque()
    queue.append(x)
    arr[x]=1

    while queue:
        x=queue.popleft()
        nx=[x+1, x-1, x*2]
        if x+1 == k or x-1 == k or x*2==k:
            arr[k]=arr[x]+1
            break
        for i in nx:
            if i>0 and i<len(arr) and arr[i]==0:
                queue.append(i)
                arr[i] = arr[x]+1

    return arr[k]-1

if n==k:
    print(0)
else: 
    print(bfs(n))
