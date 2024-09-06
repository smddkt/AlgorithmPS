n = int(input())
arr=[0]

for _ in range(n):
    arr.append(int(input()))
print(arr)

a=0
res=0
res_storage=[]

def dp(a, n, res):
    while a<n:
        if arr[a+1] > arr[a+2]:
            res+=arr[a+1]+arr[a+3]
            a+=3
            dp(a+3, n, res)
        else: 
            res+=arr[a+2]
            a+=2
            dp(a+2, n, res)
    
    res_storage.append(res)
    print(res_storage)

dp(a, n, res)
print(max(res_storage))