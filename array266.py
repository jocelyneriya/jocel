from itertools import product
n=int(input())
if(n==1):
    print(3)
    exit()
if(n==2):
    print(4)
    exit()
index=0
for i in range(1,n):
    if(n<=(2**i)):
        index=i
        break
    else:
        n=n-(2**i)
t=[]
l=list(product([3,4],repeat=index))
for i in range(0,len(l)):
    if(i==n-1):
        for j in range(0,len(l[i])):
            t.append(str(l[i][j]))
        print("".join(t))
        break
