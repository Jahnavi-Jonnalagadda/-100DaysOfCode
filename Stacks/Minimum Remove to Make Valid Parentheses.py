s = "(a(b(c)d)"

min_str = ""
open_cnt = 0

for i in s:
    if i == "(":
        open_cnt = open_cnt + 1
    elif i == ")":
        if open_cnt == 0:
            continue
        else:
            open_cnt = open_cnt - 1

    min_str = min_str + i

fin_str = ""
open_cnt = open_cnt - 1
for i in range(len(min_str)-1,-1,-1):
    
    if min_str[i] == "(" and open_cnt>0:
        continue
    fin_str = fin_str + min_str[i]

print(fin_str[::-1])

# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
