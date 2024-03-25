arr=[]
for i in range(10):
    arr.append(input(int()))

arr=list(map(int,str(arr)))
         
a=0
   
for i in range(9):
    a+=arr[i]
    if abs(a-100)>abs(a+arr[i+1]-100):
        continue
    print(abs(a+arr[i+1]-100))