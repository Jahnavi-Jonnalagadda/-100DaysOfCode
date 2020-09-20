def findJudge(N, trust):
        dct = {}
        for i in range(1, N+1):
            dct[i] = 0
        for i in range(len(trust)):
            dct[trust[i][0]] -= 1
            dct[trust[i][1]] += 1
        for item in dct:
            if(dct[item] == N-1):
                return item
        return -1
N = int(input())
trust = list(map(int,input().split()))
