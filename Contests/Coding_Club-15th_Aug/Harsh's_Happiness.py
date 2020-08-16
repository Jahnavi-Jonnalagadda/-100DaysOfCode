# Contest Link - https://www.hackerrank.com/contests/all-india-contest-by-mission-helix-15-august/challenges

def harsh_happy(arr, k):
    for j in range(len(arr)):
        if(arr[j]>k):
            return True
    return False

t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    if(harsh_happy(arr,k) == True):
        print("Yes")
    else:
        print("No")
