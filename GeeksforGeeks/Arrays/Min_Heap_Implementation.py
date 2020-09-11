def minHeapify(arr, i):
    leftChild = 2*i + 1
    rightChild = 2*i + 2
    size = len(arr)-1
    smallest = i
    
    if(leftChild <= size and arr[leftChild] < arr[i]):
        smallest = leftChild
    if(rightChild <= size and arr[rightChild] < arr[smallest]):
        smallest = rightChild
    if(smallest != i):
        arr[i], arr[smallest] = arr[smallest], arr[i]
        minHeapify(arr, smallest)

def buildMinHeap(arr):
    for i in range((len(arr)//2)-1, -1, -1):
        minHeapify(arr, i)
    return arr

def extractMin(arr):
    mn = arr[0]
    arr[0], arr[len(arr)-1] = arr[len(arr)-1], arr[0]
    arr.pop()
    return mn

arr = list(map(int, input().split()))
print(buildMinHeap(arr))
print(extractMin(arr))

        
