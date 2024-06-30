#1부터 n까지 자연수 중 중복 없이 m개 => 조합을 한 줄에 하나씩 출력


#1. itertools - 순열 이용해서 구하기
from itertools import permutations

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
combis = permutations(arr, m)

for combi in combis:
    for k in range(len(combi)):
        if k+1 == len(combi):
            print(combi[k], end = '\n')
        else:
            print(combi[k], end = ' ')


#2. 백트래킹 알고리즘 이용해서 구하기.
#백트래킹은 가능한 모든 경우를 실행해보는 것이라고 함.

