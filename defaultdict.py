dict = {1:'You', 2: 'and', 3: 'I'}
print(dict)
print(dict[1])

'''
<결과>
{1: 'You', 2: 'and', 3: 'I'}
You
'''

'''
딕셔너리에서 키 값은 고유하고, 변경할 수 없는 값이어야 한다. 
파이썬에서 튜플은 키 값이 될 수 있지만 리스트는 키가 될 수 없다.
파이썬 defaultdict모듈을 사용하면 key 값이 기본값으로 설정되기 때문에 어떤 키 값에 접근해도 에러가 발생하지 않는다. 
'''

from collections import defaultdict
letters = 'good mornig'
letters_dict = defaultdict(int)

for k in letters:
	letters_dict[k] +=1

print(letters_dict)

'''
defaultdict(<class 'int'>, {'g': 2, 'o': 3, 'd': 1, ' ': 1, 'm': 1, 'r': 1, 'n': 1, 'i': 1})
'''


#defaultdict를 사용하지 않는다면?

letters = 'good mornig'
letters_dict = {}

for k in letters:
	if not k in letters_dict:
		letters_dict[k] = 0   #이렇게 키가 존재하지 않으면 0으로 초기화해라!라는 코드가 추가로 필요함
	letters_dict[k] +=1

print(letters_dict)




#리스트에서 성씨별로 이름을 분류하기.

name_list = [('kang', 'julien'),('lee', 'junhyuck'), ('lee', 'jihoon'), ('lee', 'jihoon'), ('lee', 'jihoon'), ('jung', 'boseok'), ('shin', 'sekyeong')]
name_dict = defaultdict(list)

for key, value in name_list:
	name_dict[key].append(value)
	
print(name_dict)

'''
defaultdict(<class 'list'>, {'kang': ['julien'], 'lee': ['junhyuck', 'jihoon', 'jihoon', 'jihoon'], 'jung': ['boseok'], 'shin': ['sekyeong']})
'''



#위의 리스트의 요소를 중복 제거해서 딕셔너리에 넣고 싶다면? 
# list는 그대로 두고 defaultdict의 기본값을 set으로 하면 됨. 

name_list = [('kang', 'julien'),('lee', 'junhyuck'), ('lee', 'jihoon'), ('lee', 'jihoon'), ('lee', 'jihoon'), ('jung', 'boseok'), ('shin', 'sekyeong')]
name_dict = defaultdict(set)

for key, value in name_list:
	name_dict[key].add(value)
	
print(name_dict)

'''
defaultdict(<class 'set'>, {'kang': {'julien'}, 'lee': {'jihoon', 'junhyuck'}, 'jung': {'boseok'}, 'shin': {'sekyeong'}})
'''



#단어들을 글자수에 따라 분류하기

def group_words(words):
	grouper = defaultdict(list)
	for word in words:
		length = len(word)
		grouper[length].append(word)
	return grouper

print(group_words(["banana", "strawberry", "mango", "pineapple", "watermelon", "blueberry", "kiwi", "grapefruit"]))
'''
defaultdict(<class 'list'>, {6: ['banana'], 10: ['strawberry', 'watermelon', 'grapefruit'], 5: ['mango'], 9: ['pineapple', 'blueberry'], 4: ['kiwi']})
'''
