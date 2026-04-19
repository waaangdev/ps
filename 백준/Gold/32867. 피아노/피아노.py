n,k = input().split()
k=int(k)
li = list(map(int,input().split()))
l=r=-k
rr = -1
for i in li:
    l=min(l,i)
    r=max(r,i)
    if(r >= l+k):l=r=i;rr+=1
print(rr)