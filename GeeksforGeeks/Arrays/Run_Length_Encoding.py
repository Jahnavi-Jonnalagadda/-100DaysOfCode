def encode(arr)
    count = 0
    st = []
    p = 0
    q = 0
    while(p<len(arr) and q<len(arr)):
        if(arr[p] == arr[q]):
            count += 1
            q += 1
        else:
            st.append(arr[p])
            st.append(str(count))
            p = q
            count = 0
    st.append(arr[p])
    st.append(str(count))
    s = "".join(st)
    return s
