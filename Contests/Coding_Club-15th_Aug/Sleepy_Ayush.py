# Contest Link - https://www.hackerrank.com/contests/all-india-contest-by-mission-helix-15-august/challenges

t = int(input())
for i in range(t):
    t1 = input()
    t2 = input()
    h1, m1 = int(t1[0]+t1[1]), int(t1[3]+t1[4])
    h2, m2 = int(t2[0]+t2[1]), int(t2[3]+t2[4])
    time1 = h1*60 + m1
    time2 = h2*60 + m2
    diff = time2 - time1
    if(diff<0):
        diff += 1440
    print(str(diff//60) + " hours " + str(diff%60) + " minutes")
