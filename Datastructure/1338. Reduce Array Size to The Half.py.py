from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        res = 0
        counter = Counter(arr)
        counter = counter.most_common()

        for i in range(len(counter)):
            res += counter[i][1]
            if res >= (len(arr)//2):
                break

        return i+1




'''
num_list = [1, 2, 3, 4, 4, 4]
딕셔너리 이름 = Counter(num_list)
라고 하면 

결과: Counter({4: 3, 1: 1, 2: 1, 3: 1})


딕셔너리 이름 = dict(Counter(num_list))
라고 하면

결과: {4: 3, 1: 1, 2: 1, 3: 1}
이렇게 깔끔한 딕셔너리만 나오게 된다. 



딕셔너리를 등장 횟수 순, 즉 키/값 중 값(value) 순으로 정렬하고 싶을 때,

두 가지 방법을 쓸 수 있다. 


첫 번째는 sorted 안에서 lambda 함수로 정렬의 기준을 정해주는 것이다. 

람다 함수 사용 방법을 자꾸 까먹는데 value 값이 아니라 key 값을 기준으로 정렬해야 할 때도 있어서 꼭 익숙해져야 한다. 

sorted_list = sorted(counter.items(), key=lambda x: -x[1])

sorted_list = sorted(counter.items(), reverse = True, key = lambda x: x[1])

내림차순으로 정렬하고 싶은 거니까, 
원래 오름차순으로 정렬되는 sorted() 함수에 reverse=True 옵션을 먹이거나, 
람다 함수에서 매개변수에 - 붙인 값을 주면 된다. 그러면 절댓값이 높은 음수가 앞으로 가게 되니까 결국 내림차순 정렬 하는 것과 같은 효과를 준다고 한다.
나는 그냥 reverse = True 쓰는 게 더 편한 것 같다.



두 번째는 파이썬에 내장되어 있는 Counter.most_common() 기능을 사용하는 것이다. 
counter 딕셔너리가 자동으로 빈도가 많은 것부터 적은 것 순으로 정렬된다. 

counter = counter.most_common() 
이런 식으로 쓰면 됨.

'''
