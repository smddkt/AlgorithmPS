class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        a=0
        b=0
        res=0
        for i in s:
            if i == '(':
                a+=1
            else: b+=1
        res+=abs(a-b)

        for j in range(min(a,b)):
            if s[j]==")":
                res+=2
        return res