class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        d = collections.deque([i for i in range(1, n + 1)])
        while(len(d) != 1):
            d.rotate(-k)
            d.pop()
        return d.pop() 
        