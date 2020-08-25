def daily_temp(arr):
    p = len(arr)-1
    res = [0]*len(arr)
    st = []
    while(p >= 0):
        while(len(st)>0 and arr[p] >= st[len(st)-1][0]):
            st.pop()
        if(len(st) > 0 and arr[p] < st[len(st)-1][0]):
            res[p] = st[-1][1] - p
        st.append([arr[p], p])
        p -= 1
    return res

arr = list(map(int,input().split()))
print(daily_temp(arr))
