S = "((("

stack = []

open_cnt = 0
for i in S:
    if i == "(":
        stack.append(i)
        open_cnt = open_cnt + 1
    elif i == ")":
        if open_cnt>0 and len(stack)!=0 :
            open_cnt = open_cnt - 1
            stack.pop()
        elif open_cnt == 0 and len(stack)==0:
            open_cnt = open_cnt + 1
        elif open_cnt>0 and len(stack)==0:
            open_cnt = open_cnt + 1

print(open_cnt)
            
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
