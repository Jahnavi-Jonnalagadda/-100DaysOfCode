def repeated_char(s):
    dct = {}
    for i in s:
        if i not in dct:
            dct[i] = 1
        else:
            dct[i] += 1
    print(dct)
    for i in dct:
        if(dct[i]>1):
            return i
    return -1

t = int(input())
for i in range(t):
    string = input()
    print(repeated_char(string))
