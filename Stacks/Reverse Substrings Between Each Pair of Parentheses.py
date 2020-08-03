s = "a(bcdefghijkl(mno)p)q"

stack = []
top = -1
for i in s:
    if i == "(" or i.isalpha():
        stack.append(i)
    elif i == ")":
        l = []
        while stack[top] != "(":
            l.append(stack[top])
            stack.pop()
        stack.pop()
        while len(l) != 0:
            stack.append(l[0])
            l.pop(0)

fin_str = "".join(stack)
print(fin_str)
            
            
# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
