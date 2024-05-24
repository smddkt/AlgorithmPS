import heapq

def solution(scoville, k):
    heapq.heapify(scoville)
    count=0
    while scoville[0]<k:
        if len(scoville)==1:
            return -1
        a=heapq.heappop(scoville)
        b=heapq.heappop(scoville)
        heapq.heappush(scoville, a+(b*2))
        count+=1
    return count