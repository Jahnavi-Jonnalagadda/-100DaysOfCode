def oneAway(s1, s2):
    if(len(s1) == len(s2)):
        return oneReplace(s1, s2)
    elif(len(s1)+1 == len(s2)):
        return oneInsert(s1, s2)
    elif(len(s1)-1 == len(s2)):
        return oneInsert(s2, s1)
    return False

def oneReplace(s1, s2):
    flag = False
    for i in range(len(s1)):
        if(s1[i] == s2[i]):
            flag = True
        else:
            if(flag == False):
                flag = True
            else:
                return False
    return True

def oneInsert(s1, s2):
    i1, i2 = 0, 0
    while(i1 < len(s1) and i2 < len(s2)):
        if(s1[i1] == s2[i2]):
            i1 += 1
            i2 += 1
        else:
            if(i1 == i2):
                i2 += 1
            else:
                return False
    return True

s1 = input()
s2 = input()
print(oneAway(s1, s2))
            
