import sys
import heapq

input=sys.stdin.readline

n=int(input())
min_heap=[]

for i in range(n):
    heapq.heappush(min_heap, int(input()))

res=0
while len(min_heap)>=2:
    a= heapq.heappop(min_heap)
    b= heapq.heappop(min_heap)
    res+=(a+b)
    heapq.heappush(min_heap, (a+b))


print(res)








