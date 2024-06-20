from collections import Counter

class Solution:
    def topKFrequent(self, nums:List[int], k:int) -> List[int]:
        numDict = dict(Counter(nums))
        countlist = sorted(numDict.items(), reverse = True, key = lambda x: x[1])
        res=[]
        for i in range(k):
            res.append(countlist[i][0])
        return res