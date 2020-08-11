arr = [1, 12, 4, 6, 7, 10]
arr.sort()

start = 0
end = len(arr)-1

l = []
while(start<end):
    l.append(arr[end])
    l.append(arr[start])
    end -= 1
    start += 1

if(len(arr)%2 != 0):
    l.append(arr[start])

print(l)
