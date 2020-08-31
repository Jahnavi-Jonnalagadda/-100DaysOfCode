def subset_sum(A, B):
        dp = []
        n = len(A)
        # append rows
        for i in range(n+1):
            dp.append([])
        
        # append columns and initialization
        for i in range(n+1):
            for j in range(B+1):
                if(i == 0 and j == 0):
                    dp[i].append(1)
                elif(i == 0 and j!=0):
                    dp[i].append(0)
                elif(i != 0 and j==0):
                    dp[i].append(1)
                else:
                    dp[i].append(-1)
                    
        # choice diagram
        for i in range(1, n+1):
            for j in range(1, B+1):
                if(A[i-1]<=j):
                    dp[i][j] = dp[i-1][j-A[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[i][j]

A = list(map(int,input().split()))
B = int(input())
print(subset_sum(A, B))
