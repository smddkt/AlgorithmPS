def solution(s):
    isTrue=False
    stack=[]
    
    if s[0]=="(":
        stack.append(s[0])
    else:
        return isTrue
    
    for i in range(1, len(s)):
        if s[i]=="(":
            stack.append(s[i])
        else: 
            if len(stack)==0:
                return isTrue
            stack.pop()
            
    if len(stack)==0:
        isTrue=True
    return isTrue



t = int(input())

for _ in range(t):
    string=input()
    print(solution(string))


