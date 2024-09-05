from collections import deque
n = int(input())
deque=deque()

for i in range(1,n+1):
    deque.append(i)

while len(deque)>1:
    deque.popleft()
    deque.append(deque[0])
    deque.popleft()

# count = 2*n-3
# for i in range(count):
#     deque.popleft()
#     deque.append(deque[0])
#     deque.popleft()
#     if len(deque)==1:
#         break


print(deque[0])