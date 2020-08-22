arr = [1,1,1]
k = 2
l = 0
r = 0
curr_sum = 0
count = 0

while(l<=len(arr) and r<=len(arr)):
    curr_sum += arr[l]
    if(curr_sum < k):
        l += 1
    if(curr_sum == k):
        count += 1
        l += 1
        #r += 1
    while(curr_sum > k):
        curr_sum -= arr[r]
        r += 1
    print(l,r)
print(count)
