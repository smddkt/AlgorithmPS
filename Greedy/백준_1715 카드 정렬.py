import sys
input=sys.stdin.readline

n=int(input())
arr=[]

for i in range(n):
    arr.append(i)

arr=sorted(arr)

hap = arr[0]+arr[1]

del arr[0]
del arr[0]

if hap<arr[1]:
    hap=arr[0]+hap
    del arr[0]
else: 
    arr.append(hap)
    hap=arr[0]+arr[1]
    del arr[0]
    del arr[0]







