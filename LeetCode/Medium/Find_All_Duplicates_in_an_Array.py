# Time Complexity: O(N), Space Complexity: O(N)
def findDuplicates(arr):
        dct = {}
        for i in range(len(arr)):
            if arr[i] in dct:
                dct[arr[i]] += 1
            else:
                dct[arr[i]] = 1
                
        res = []
        for item in dct:
            if(dct[item] > 1):
                res.append(item)
        
        return res
arr = list(map(int,input().split()))
print(findDuplicates([1, 1]))

# Time Complexity: O(N), Space Complexity: O(1)
def findDuplicates(arr):
        res = []
        for i in range(len(arr)):
            idx = abs(arr[i]) - 1
            if(arr[idx] < 0):
                res.append(abs(arr[i]))
            else:
                arr[idx] = -1*(arr[idx])
        return res
arr = list(map(int,input().split()))
print(findDuplicates(arr))
