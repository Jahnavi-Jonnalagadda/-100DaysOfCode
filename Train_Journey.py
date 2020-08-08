dct = {1:"WS",2:"MS",3:"AS",4:"AS",5:"MS",6:"WS",7:"WS",8:"MS",9:"AS",10:"AS",
       11:"MS",12:"WS"}

t = int(input())
for i in range(t):
    n = int(input())
    if n%12 == 0:
        print(n-12+1, "WS")
    else:
        print(n+13-(2*(n%12)), dct[n%12])
