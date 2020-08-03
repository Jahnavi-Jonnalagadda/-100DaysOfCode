s = "abbaca"

k = 2

stack = []
dct = {}
for i in s:
    top = len(stack)-1
    stack.append(i)
    top = top + 1

    if i not in dct:
        dct[i] = 1
    else:
        if len(stack)>1:
            if stack[top] == stack[top-1]:
                dct[i] = dct[i] + 1
                if dct[i] == k:
                    del dct[i]
                    for j in range(k):
                        stack.pop()
        else:
            stack.append(i)
fin_str = "".join(stack)         
print(fin_str)
        
        
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/      
