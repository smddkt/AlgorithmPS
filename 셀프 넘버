arr=[]

for i in range(1,10001):
    arr.append(i)
    
for i in range(1,10001):
    a = sum(map(int,str(i))) + int(i)
    if a in arr:
        arr.remove(a)

for _ in arr:
    print(_)
    
    
    
    
    #남의 풀이
    
# n = set(range(1, 10001))

# sums = set()

# for i in range(1, 10001):
#     sums.add(sum(map(int, list(str(i)))) + i)

# result = sorted(list(n - sums))

# for i in result:
#     print(i)