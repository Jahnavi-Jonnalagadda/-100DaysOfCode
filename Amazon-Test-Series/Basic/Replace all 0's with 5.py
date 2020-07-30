n = 1004
n = list(str(n))
for i in range(len(n)-1):
    if n[i] == '0':
        n[i] = '5'
print(int(''.join(n)))
