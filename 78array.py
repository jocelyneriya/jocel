n=int(input())
m=0
for z in range(0,n):
  s=input()
  a=0
  b=0
  l=0
  i=0
  k=0
  for j in range(0,len(s)):
    if(s[j]=="a"):
      a=a+1
    elif(s[j]=="b"):
      b=b+1
    elif(s[j]=="i"):
      i=i+1
    elif(s[j]=="l"):
      l=l+1
    elif(s[j]=="k"):
      k=k+1 
  if(a==2 and b==1 and i==1 and l==1 and k==1):
    m=m+1
print(m)
