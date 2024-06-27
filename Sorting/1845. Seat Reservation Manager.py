import heapq
class SeatManager:
    def __init__(self, n: int):
        self.h = []
        for i in range(1, n+1):
            self.h.append(i)
        self.res = []
        self.res.append('null')

    def reserve(self) -> int:
        a= heapq.heappop(self.h)
        self.res.append(a)
        return a
        
    def unreserve(self, seatNumber: int) -> None:
        b = heapq.heappush(self.h, seatNumber)
        self.res.append('null')

        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)