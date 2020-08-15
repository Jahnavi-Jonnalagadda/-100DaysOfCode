t = int(input())

for p in range(t):
  n = int(input())
  count = 0
  for k in range(n):
    string = input()
    count_arr = [0]*26
    
    for i in string:
        count_arr[ord(i)-ord("a")] += 1

    odd = 0
    for j in range(len(count_arr)):
        if(count_arr[j]%2 != 0):
            odd += 1
            
    if(odd == 0 or odd == 1):
        count += 1
  print(count)
