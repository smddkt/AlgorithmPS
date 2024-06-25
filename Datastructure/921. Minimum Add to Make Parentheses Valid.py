class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        res=0
        for i in s:
            if i=="(":
                stack.append("(")
            else: 
                if stack:
                    stack.pop()
                else: res+=1
        res+=len(stack)

        return res


"""
string s의 원소를 순회하면서, 

1. 여는 괄호가 나오면 stack에 추가한다.

2. 닫는 괄호가 나오면 stack에서 여는 괄호 한 개를 pop한다. 

3. 만약 pop하기 전에 stack이 비어 있으면 여는 괄호 하나를 어딘가에 추가해야 한다는 뜻이므로 res에 1씩 더한다. 

4. 순회를 모두 마치고, stack에 있는 여는 괄호가 모두 소거되지 않고 남아있을 수 있다. 
그러면 그 수만큼 닫는 괄호를 추가해야 한다는 뜻이므로 len(stack)을 res에 다시 더해 준다. 
"""