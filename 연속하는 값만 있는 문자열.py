n=int(input())
a=0
for i in range(n):
    d=input()
    for i in d:
        cnt=d.count(i)
        if cnt==1:
            a+=0
            break
        elif cnt>1:
            for j in range(1,cnt):
                if i!=d[d.index(i)+j]:
                    a+=1
            break

print(n-a)
                    