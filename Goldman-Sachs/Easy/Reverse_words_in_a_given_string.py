t = int(input())
for i in range(t):
    string = input()
    l = []
    text = ""
    for x in string:
        if x != ".":
            text = text + x
        else:
            l.append(text)
            l.append(".")
            text = ""
    if(text!=""):
        l.append(text)
    print("".join(l[::-1]))
    
