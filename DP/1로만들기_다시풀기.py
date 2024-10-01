# 1로 만들기. 3으로 나누거나 2로 나누거나 1을 빼서 최종적으로 1이 되도록 하는 최소 연산 횟수 구하기

# 1에서 1 더하거나 2 곱하거나 3 곱한 수에서 1을 더하거나 2를 곱하거나 3을 곱한 수에서... 이런 식으로 가다가 몇 번째에 입력값 N이 등장하는지를 따져봐도 될 것 같다. 
# 이렇게 하면 메모리 초과됨. 하나당 세개씩 늘어나니까..말도 안되게 큰 배열...
n = int(input())
arr1 = set([1])
arr2 = set()
count = 1

while n not in arr1 and n not in arr2: 
    arr2 = set()
    is_break = False
    for i in arr1:
        arr2.add(i+1)
        arr2.add(i*2)
        arr2.add(i*3)
        if n in arr2:
            is_break = True
            break
    if is_break==True: 
        break
    else:
        count += 1 
    arr1 = set()
    for j in arr2:
        arr1.add(j+1)
        arr1.add(j*2)
        arr1.add(j*3)
        if n in arr1:
            is_break = True
            break
    if is_break==True:
        break
    else: 
        count += 1

if n == 1: print(0)
else: 
    print(count)


# DP를 이용하는 건데.. arr이라는 배열 자체를 업데이트하는데 이 배열의 n 번째 원소의 값 = n을 1로 만드는데 필요한 최소 연산 횟수
# 이렇게 보면 이게 DP가 아닐 수 없는 문제였던 것임....

n = int(input())

arr = [0 for _ in range(n+1)]

for i in range(2, n+1):
    arr[i] = arr[i-1] + 1

    if i%2==0:
        arr[i] = min(arr[i], arr[i//2]+1)
    if i%3==0:
        arr[i] = min(arr[i], arr[i//3]+1)

print(arr[n])
    