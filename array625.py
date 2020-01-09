q=int(input())
l=[]
r=[]
for _ in range(q):
    t=list(map(int,input().split()))
    if(t[0]==1):
        l.append(t[1])
    elif(t[0]==2):
        if(len(l)>0):
            r.append(min(l))
        else:
            r.append(-1)
print(*r)
