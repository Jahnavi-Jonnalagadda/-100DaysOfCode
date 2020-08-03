def decodeString(s: str) -> str:
        num = []
        char = []
        for i in s:
            if i == "[":
                num.append("[")
                char.append("[")
            elif i.isnumeric():
                num.append(i)
            elif i.isalpha():
                char.append(i)
            elif i == "]":                
                c = ""
                print(char[-1])
                while char[-1] != "[":
                    c = char.pop() + c
                char.pop()
                n = ""
                num.pop()
                while len(num) > 0 and num[-1] != "[":
                    n = num.pop() + n
                # print("".join([c for i in range(int(n))]))
                char.append("".join([c for i in range(int(n))]))
        
        return "".join([i for i in char])
print(decodeString("2[abc]3[cd]ef)"))

# https://leetcode.com/problems/decode-string/
