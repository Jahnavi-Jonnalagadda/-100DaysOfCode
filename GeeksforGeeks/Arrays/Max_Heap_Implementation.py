def maxHeapify(arr, i):
    leftChild = 2*i + 1
    rightChild = 2*i + 2
    size = len(arr)-1
    largest = i
    if(leftChild <= size and arr[leftChild] > arr[i]):
        largest = leftChild
    if(rightChild <= size and arr[rightChild] > arr[largest]):
        largest = rightChild
    if(largest != i):
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, largest)

def buildMaxHeap(arr):
    for i in range((len(arr)//2)-1, -1, -1):
        maxHeapify(arr, i)
    print("Max Heap: ", arr)

def extractMax(arr):
    if(len(arr) == 0):
        return -1
    mx = arr[0]
    arr[0] = arr[len(arr)-1]
    arr.pop()
    return mx

arr = list(map(int,input().split()))
buildMaxHeap(arr)
print("Max element: ", extractMax(arr))
