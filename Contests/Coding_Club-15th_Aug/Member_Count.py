# Contest Link - https://www.hackerrank.com/contests/all-india-contest-by-mission-helix-15-august/challenges

def member_count(n):
    i = 1
    while(((i*(i-1))//2) <= n):
        if(((i*(i-1))//2) == n):
            return True
        i += 1
    return False

t = int(input())
for i in range(t):
    n = int(input())
    if(member_count(n) == True):
        print("Possible")
    else:
        print("Impossible")
    
