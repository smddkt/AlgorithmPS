#스코빌지수가 가장 낮은 거 + 두 번째로 낮은 거*2 합치기. 모든 음식의 스코빌지수가 k가 넘을 때까지
# heapq 쓰면 좋은 점: 더해서 나온 값이 정렬된 리스트에서 제자리를 찾아서 들어가야 계속해서 스코빌지수가 제일 낮은 음식을 heappop으로 구할 수 있다.
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
