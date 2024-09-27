n,m=map(int,input().split())

arr=list(map(int,input().split()))

arr_2=[]

for i in arr:
    for j in arr:
        for k in arr:
            if i+j+k<=m and i!=j and j!=k and k!=i:
                arr_2.append(i+j+k)
                
arr_2.sort(reverse=True)                
print(arr_2[0])
                
    
    
    
n, m = map(int, input().split())
a = list(map(int, input().split()))
max = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if a[i] + a[j] + a[k] > m:
                pass
            else:
                sum = a[i] + a[j] + a[k]
                if sum > max:
                    max = sum
print(max)


from itertools import combinations

cond = list(map(int, input().split()))
nums = list(map(int, input().split()))

            
combi = list(combinations(nums, 3))
sum_combi=[sum(x) for x in combi if sum(x)<=cond[1]]

print(max(sum_combi))