n = int(input())
five = (n-4)//5
if(n - five*5)%2 == 0:
    one = 2
else:
    one = 1

two = (n - five*5 - one*1)//2
total = one+two+five
print(total, five, two, one)
