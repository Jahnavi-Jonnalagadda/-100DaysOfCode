'''n = int(input())
dp = [0]*(n+1)
dp[0] = 1
dp[1] = 1
        
for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])'''

n = 4
p0 = 1
p1 = 1

for i in range(1,n):
    c1 = p0
    c0 = p0 + p1
    p1 = p0
    p0 = p0 + p1

if(n == 1):
    print(p0+p1)
else:
    print(c0+c1)
