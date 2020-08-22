n,m = map(int, input().split())
count = 0
val = len(str(n))*9 + 1
for i in range(n+val,m+1):
    m = str(m)
    l = len(str(n))
    l = -1*l
    i = str(i)
    if(i[l:] == str(n)):
        count += 1
print(count+1)
