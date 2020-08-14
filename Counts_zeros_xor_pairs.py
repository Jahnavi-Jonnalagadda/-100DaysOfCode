#code
from collections import Counter

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    c = Counter(arr)
    dct = dict(c.items())
    
    count = 0
    for item in dct:
        if dct[item]>1:
            count += (dct[item])*(dct[item]-1)//2
            
    print(count)
