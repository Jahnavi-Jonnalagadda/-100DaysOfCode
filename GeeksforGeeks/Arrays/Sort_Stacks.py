def sort_stack(st):
    s = []
    while(len(st) > 0):
        top = st.pop()
        if(len(s) > 0):
            if(top <= s[-1]):
                s.append(top)
            else:
                while(len(s)>0 and top > s[-1]):
                    st.append(s.pop())
                s.append(top)
        else:
            s.append(top)
    return s[::-1]

# Compressed the above solution - (same approach)
def sort_stack(st):
    if(len(st) == 0):
        return st
    s = []
    s.append(st.pop())
    while(len(st) > 0):
        top = st.pop()
        while(len(s)>0 and top > s[-1]):
            st.append(s.pop())
        s.append(top)
    return s[::-1]

st = list(map(int,input().split()))
print(sort_stack(st))

                    
