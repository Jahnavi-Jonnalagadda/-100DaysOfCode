import sys
def reverse(ar,i):
    l = len(ar)-1
    while i<l:
        ar[i],ar[l] = ar[l],ar[i]
        i += 1
        l -= 1 

ar = [6,2,1,5,4,3,0]
i = len(ar)-1
while ar[i]<ar[i-1] and i>0:
    i -= 1

if i>0:
    l = len(ar)-1
    while l>=i:
        if ar[l]>ar[i-1]:
            ar[l],ar[i-1] = ar[i-1],ar[l]
            break
        l -= 1
reverse(ar,i)
    
print(ar)
