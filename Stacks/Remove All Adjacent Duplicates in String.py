S = "abbaca"

stack = []

for i in S:
    if len(stack) == 0:
        stack.append(i)
    else:
        if stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
fin_str = "".join(stack)
print(fin_str)

# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
