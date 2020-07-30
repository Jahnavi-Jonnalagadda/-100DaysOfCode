arr = [1,2,3,4,5]
int_min = -2147483648

l1 = int_min
l2 = int_min

for i in range(len(arr)):
    if(arr[i]==l1 or arr[i]==l2):
        continue
    else:
        if(arr[i]>l1):
            l2 = l1
            l1 = arr[i]
        elif(arr[i]>l2):
            l2 = arr[i]
if(l1==int_min):
    l1 = -1
elif(l2==int_min):
    l2 = -1
print([l1, l2])
