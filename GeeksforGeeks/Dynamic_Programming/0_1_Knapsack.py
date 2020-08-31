def 01knapsack(item, weight, capacity):
        n = len(A)
        dp = []
        
        # append rows
        for i in range(n+1):
            dp.append([])
        
        # append columns
        for i in range(n+1):
            for j in range(C+1):
                if(i == 0 or j == 0): #initialization
                    dp[i].append(0)
                else:
                    dp[i].append(-1)
        
        # choice diagram
        for i in range(1, n+1):
            for j in range(C+1):
                if(B[i-1]<=j):
                    dp[i][j] = max(A[i-1]+dp[i-1][j-B[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[i][j]

item = list(map(int, input().split()))
weight = list(map(int, input().split()))
capacity = int(input())
print(01knapsack(item, weight, capacity))
