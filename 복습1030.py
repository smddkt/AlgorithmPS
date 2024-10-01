#요세푸스 문제
from collections import deque

n, k = map(int, input().split())
arr=deque([i for i in range(1, n+1)])

yosep = []

while len(arr)>0:
    arr.rotate(-(k-1))
    yosep.append(arr.popleft())

#rotate할 때 양수는 오른쪽으로 미는 거, 음수는 왼쪽으로 미는 거. 직관적으로 왠지 그럴 것 같은 방향임.


#join이라는 게 있음. 이게 뭐냐면 리스트에 있는 각각의 원소들을 한번에 출력할 수 있게 해주는 메서드인데
# join앞에다가 구분자를 쓸 수 있음. 이 경우에는 출력을 쉼표를 넣어서 하면 됨.
# 그리고 원래 이 기능은 문자열이 원소일 때만 사용 가능하므로 지금은 map이용해서 숫자를 문자열로 바꾼 다음에 출력해야 함.
print("<" + ", ".join(map(str, yosep))+ ">")




# 길이순, 사전순 정렬이라고 문제에는 나와있지만 사전순 길이순으로 해도 결과는 같고 또 그렇게 하는 것이 훨씬 더 쉽다. 
from collections import defaultdict
n = int(input())
words = [input() for _ in range(n)]
words.sort()

dict = defaultdict(set)

for word in words: 
    length = len(word)
    dict[length].add(word)

for length in sorted(dict.keys()):
    for word in sorted(dict[length]):
        print(word)
"""
과정 정리: 
1. 입력되는대로 단어를 추가한 리스트를 만든다.
2. 그 리스트의 단어들을 사전순으로 정렬한다.
3. 딕셔너리를 하나 초기화한다.
4. 각 단어의 길이를 키로, 그 길이를 가진 단어들을 value로 딕셔너리를 채운다.
5. 그.. key값(단어길이)를 기준으로 정렬한 length별로 그에 해당하는 word를 하나씩 프린트한다.
6. 그러면 이미 처음부터 사전순 정렬된 리스트였기 때문에 길이순+사전순으로 프린트가 됨.
"""


#아래는 6개월 전에 푼 코드이다. 람다는 솔직히. 검색 안하면 쓰는 법을 계속 까먹는다.
n= int(input())
arr=[]

for _ in range(n):
    arr.append(str(input())) #단어 입력받아서 리스트에 넣기

arr=list(set(arr)) #중복되는 단어 삭제
arr.sort() #알파벳 사전순으로 정렬


arr.sort(key = lambda i:len(i)) #알파벳 길이순으로 정렬

for i in arr:
    print(i)




#그룹단어체커: 그룹단어는 각 문자들이 단어 안에서 나눠서 등장하는 게 아니라 한번에 등장하는 단어를 말함.

n = int(input())
arr = [input() for _ in range(n)]
count = n

for word in arr:
    visited = [word[0]]
    for i in range(1, len(word)):
        if word[i] in visited and word[i-1] != word[i]:
            count -= 1
            break
        elif word[i] not in visited:
            visited.append(word[i])

print(count)
    





#다솜이가 문자열 뒤집는 문제 : 최소 행동 횟수는?
#0 그룹의 개수와 1그룹의 개수 중 더 작은 걸 뒤집으면 됨. --> 더 작은 그룹의 개수를 출력하기

str = input()

def mincount(str):
    count0 = 0
    count1 = 0
    if str[0] == '1':
        count1 += 1
    else: count0 += 1

    for i in range(1, len(str)):
        if str[i-1] != str[i]:
            if str[i] == '0':
                count0 += 1
            else: count1 += 1
        else: continue
    return min(count0, count1)

if len(str) ==1:
    print(0)    
else: print(mincount(str))
'''
예외처리를 잘 해야 한다.. 작년에는 한 번에 푼 걸 지금은 몇 번 틀렸다. 
아이디어는 맞는 방향으로 가고 있었는데
1. str자체가 한 문자만으로 구성된 경우를 고려하지 않았고,
2. if문에 해당하지 않으면 반복문의 다음 구간으로 바로 넘어가게 하지도 않았다.
'''