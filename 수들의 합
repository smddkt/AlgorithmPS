t=int(input())

for i in range(t):
    a,b=map(int,input().split())
    
    i=0
    j=0
        
    if a>=b:
        while True:
            if a%a==0 and a%b==0:
                i=a
                break
            else: a+=1
    else:
        while True:
            if b%a==0 and b%b==0:
                i=b
                break
            else: b+=1
            
    if a>=b:
        while True:
            if a%b==0 and b%b==0:
                j=b
                break
            else: b-=1
    else:
        while True:
            if a%a==0 and b%a==0:
                j=a
                break
            else: a-=1           
    
    print(i,j)
        
