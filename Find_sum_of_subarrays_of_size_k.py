l = [1,3,4,2,6,3]
k = 3
s = []
tot = 0
tot = sum(l[:k])
'''for i in range(k):
    tot += l[i]'''
s.append(tot)

for i in range(k):
    tot = tot - l[i] + l[i+k]
    s.append(tot)

print(s)
    
