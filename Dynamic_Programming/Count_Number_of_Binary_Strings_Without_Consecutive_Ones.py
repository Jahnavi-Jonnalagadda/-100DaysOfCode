#Space complexity = O(n)
n = 4
dp0 = [0]*n
dp1 = [0]*n

dp0[0] = 1
dp1[0] = 1

for i in range(1,n):
    dp0[i] = dp0[i-1] + dp1[i-1]
    dp1[i] = dp0[i-1]
print(dp0[n-1]+dp1[n-1])


    