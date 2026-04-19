l,r=map(int,input().split())
r+=1
li=[1]*(r-l)
d=1
for i in range(3,r,2):
    d+=i
    if(d>r):break
    st=l+d-((l-1)%d)-1
    for j in range(st,r,d):li[j-l]=0
print(sum(li))
