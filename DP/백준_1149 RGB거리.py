import sys
input = sys.stdin.readline
n = int(input())

arr=[]

for i in range(n):
    arr.append(list(map(int,input().split())))
    
dp = []
for _ in range(n):
    dp.append([0, 0, 0])

dp[0][0] = arr[0][0]
dp[0][1] = arr[0][1]
dp[0][2] = arr[0][2]

for i in range(1, n):
    
    dp[i][0] = min(dp[i-1][1], dp[i-1][2])+arr[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2])+arr[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1])+arr[i][2]
    
    '''
    if dp[i-1][0]+arr[i][1] <= dp[i-1][2]+arr[i][1]:
        dp[i][1]= dp[i-1][0]+arr[i][1]
    else: dp[i][1] = dp[i-1][2]+arr[i][1]
    
    ↑ 이런 형식에서 간단하게 수정한 뒤에 시간 반으로 줄음. 
    
    '''
    
print(min(dp[n-1]))
    
