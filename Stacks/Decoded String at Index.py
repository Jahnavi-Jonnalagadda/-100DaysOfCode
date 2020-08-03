S = "leet2code3"

stack = []
temp = ""
for i in S:
    
    if i.isalpha():
        temp = temp + i
        stack.append(i)
        print(stack)
    else:
        for j in range(int(i)-1):
            pretemp = ""
            for p in temp:
                pretemp = pretemp + p
                stack.append(p)
            temp = temp + pretemp
        print(stack)

print("".join(stack))

# https://leetcode.com/problems/decoded-string-at-index/
