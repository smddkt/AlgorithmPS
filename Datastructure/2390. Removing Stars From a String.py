class Solution:
    def removeStars(self, s: str) -> str:
        s = list(s)
        q= []
        for i in s:
            if i =='*':
                q.pop()
            else: q.append(i)
        res=''
        for j in q:
            res+=(j)
        return res
    
'''
res=''
        for j in q:
            res+=(j)
        return res

이 부분을 수정하는 방법
return "".join(q)
'''