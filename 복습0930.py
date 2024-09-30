#단어의 개수 구하기
sentence = input()
if len(sentence)>=2:
    count = 1

    for i in range(1, len(sentence)-1):
        if sentence[i] == " ":
            count += 1

    print(count)
elif len(sentence)==1 and sentence[0]!=" ":
    print(1)

else: print(0)

#1년 전의 내가 만든 개 잘 짠 코드: 시간도 더 조금밖에 안 걸림. ㅋ
s=list(map(str,input().split()))
print(len(s))


# 가장 많이 사용된 알파벳 구하기

from collections import Counter
word = input()
dict = Counter(word.upper()).most_common()
count = 0
for i in dict:
    if i[1] == dict[0][1]:
        count += 1

if count >= 2:
    print("?")
else: print(dict[0][0])


#요세푸스 순열
from collections import deque
n, k = map(int, input().split())

list = deque([i for i in range(1, n+1)])

yosep = []

# while len(list)>2:
#     for _ in range(n-1):
#         list.append(list[0])
#         list.popleft()
#     yosep.append(list.popleft())

# if len(list)==2:
#     yosep.append(list[0])
#     yosep.append(list[1])

while list:
    list.rotate(-(k-1))
    yosep.append(list.popleft())

print("<" + ",".join(map(str, yosep)) + ">")