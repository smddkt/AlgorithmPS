#문제에 적힌대로 풀면 통과는 되지만 시간복잡도가 O(n^2)인 말 그대로 복잡한 풀이..

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i<j:
                    count+=1

        return count
    

#해시맵을 사용하면 시간복잡도를 O(n)으로 줄일 수 있다.

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:        
        count_dict = defaultdict(int)
        count = 0
        for num in nums:
            count += count_dict[num]
            count_dict[num] += 1
        return count

    