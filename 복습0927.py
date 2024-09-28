# #1000
a, b = map(int, input().split())
print(a+b)


# #1003
arr1=[1, 0, 1, [0]*38]
arr2=[0, 1, 1, [0]*38]

for i in range(3, 41):
    arr1[i] = arr1[i-1]+arr1[i-2]
    arr2[i] = arr2[i-1]+arr2[i-2]

n= int(input())
for _ in range(n):
    a=int(input())
    print(arr1[a], arr2[a])


#1009
n = int(input())

arr2 = [6, 2, 4, 8]
arr3 = [1, 3, 9, 7]
arr7 = [1, 7, 9, 3]
arr8 = [6, 8, 4, 2]
arr4 = [6, 4]
arr9 = [1, 9]

for _ in range(n):
    a, b = map(int, input().split())
    if a%10 == 1 or a%10 ==5 or a%10 == 6:
        print(a%10)
    elif a%10 == 2:
        print(arr2[b%4])
    elif a%10 == 3:
        print(arr3[b%4])
    elif a%10 == 7:
        print(arr7[b%4])
    elif a%10 == 8:
        print(arr8[b%4])
    elif a%10 == 4: 
        print(arr4[b%2])
    elif a%10 == 9:
        print(arr9[b%2])
    else: #a%10==0:
        print(10)



#1010 다리놓기 재원이
count = int(input())
for _ in range(count):
    num1 = 1
    num2 = 1
    n, m = map(int, input().split())
    for i in range(m-n+1, m+1):
        num1 *= i

    for j in range(1, n+1):
        num2 *= j

    print(num1//num2)



#1012

from collections import deque

case= int(input())

for _ in range(case):
    m, n, k = map(int, input().split())
    count = 0 
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    graph = [[0]*m for i in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    queue = deque([(m, n)])

    while len(queue)>=1: 
        x, y = queue.popleft()
        canmove=0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if graph[ny][nx]==1:
                queue.append((nx, ny))  
                canmove+=1  
        #만약 네 방면 모두 0이었다면?
        if canmove == 0:
            count+=1

    print(count)




