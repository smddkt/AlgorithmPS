def isStackEmpty():
    global size, stack, top 
    if (top==-1):
        return 1
    else: 
        return 0
    
def isStackFull():
    global size, stack, top
    if (top>=size-1):
        return 1
    else: 
        return 0

def push(data):
    global size, stack, top 
    top += 1
    stack[top] = data
    size+=1
    
def pop(data):
    global size, stack, top 
    if (isStackEmpty()==1):
        return -1
    data = stack[top]
    stack[top]=None
    top-=1
    size-=1
    return data

def peek():
    global size, stack, top 
    if (isStackEmpty()==1):
        return -1
    return stack[top]

import sys

n=int(sys.stdin.readline().rstrip())
top = -1
size=0
stack = [None for _ in range(n)]
    
for i in range(n):
    a = sys.stdin.readline().rstrip()
    if a=='pop':
        print(pop(stack[top]))
    if a=='size':
        print(size)
    if a=='empty':
        print(isStackEmpty())
    if a=='top':
        print(peek()) 
    if a[1]=='u':
        a=a[5:]
        push(a)      
        
