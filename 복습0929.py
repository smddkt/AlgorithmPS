#한수 : 양의 정수 x의 각 자리가 등차수열을 이루는 수. n이 주어졌을 때 ..1부터 n까지 한수의 개수 출력하기

n = int(input())
#1부터 99까지는 한수이다. 

hansu = [111, 123, 135, 147, 159, 210, 222, 234, 246, 258, 321, 333, 345, 357, 369, 420, 432, 444, 456, 468, 531, 543, 555, 567, 579, 630, 642, 654, 666, 678, 741, 753, 765, 777, 789, 840, 852, 864, 876, 888, 951, 963, 975, 987, 999]
count = 0

if n < 100:
    print(n)
else:
    count+=99
    for i in range(len(hansu)):
        if hansu[i]<=n:
            count+=1
        else: break

    print(count)



#RGB거리: 빨/초/파 중 하나의 색으로 칠해야 한다. 이웃한 집들과는 색이 달라야 한다.

import sys
input = sys.stdin.readline
n = int(input())

arr=[]

for i in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0, 0, 0] for _ in range(n)] #min_arr
dp[0] = arr[0]


for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]

print(min(dp[n-1]))