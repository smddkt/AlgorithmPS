n = int(input())

arr=[]

for i in range(n):
    arr.append(list(map(int,input().split())))
    
min_arr = []
for _ in range(n):
    min_arr.append([0, 0, 0])

min_arr[0][0] = arr[0][0]
min_arr[0][1] = arr[0][1]
min_arr[0][2] = arr[0][2]

for i in range(1, n):
    
    if min_arr[i-1][0]+arr[i][2] <= min_arr[i-1][1]+arr[i][2]:
        min_arr[i][2]= min_arr[i-1][0]+arr[i][2]
    else: min_arr[i][2] = min_arr[i-1][1]+arr[i][2]
    
    if min_arr[i-1][1]+arr[i][0] <= min_arr[i-1][2]+arr[i][0]:
        min_arr[i][0]= min_arr[i-1][1]+arr[i][0]
    else: min_arr[i][0] = min_arr[i-1][2]+arr[i][0]
    
    if min_arr[i-1][0]+arr[i][1] <= min_arr[i-1][2]+arr[i][1]:
        min_arr[i][1]= min_arr[i-1][0]+arr[i][1]
    else: min_arr[i][1] = min_arr[i-1][2]+arr[i][1]
    
print(min(min_arr[n-1]))




# if arr[0][0]+arr[i][2] <= arr[0][1]+arr[1][2]:
#         min2=arr[0][0]+arr[1][2]
#     else: min2 = arr[0][1]+arr[1][2]

#     if arr[0][0]+arr[1][1] <= arr[0][2]+arr[1][1]:
#         min1=arr[0][0]+arr[1][2]
#     else: min1 = arr[0][2]+arr[1][1]

#     if arr[0][1]+arr[1][0] <=arr[0][2]+arr[1][0]:
#         min0 = arr[0][1]+arr[1][0]
#     else: min0 = arr[0][2]+arr[1][0]
    
