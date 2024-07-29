k=int(input().rstrip())
arr=[]
for i in range(k):
    n=int(input().rstrip())
    if n==0:
        del arr[-1]
    else:
        arr.append(n)

print(sum(arr))


