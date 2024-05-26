#max_heapify 함수

def max_heapify(arr, n, i):
    largest = i
    left = 2 * i +1
    right = 2 * 1 + 2

    if left < n and arr[largest] < arr[left]:
        largest = left
    
    if right < n and arr[largest] < arr[right]:
        largest = right
    
    if largest != i :
        arr[i], arr[largest] = arr[largest], arr[i]
        #왼쪽이 크든 오른쪽이 크든 둘 중 더 큰 것 하나랑만 힙 트리에서 자리를 바꾼다.
        #노드 교환 후에는 그냥 계속 max_heapify를 재귀적으로 호출한다.