s=int(input())
m=[[0]*9,[0]*9]
r=0
for i in m[0]:
    x,y=list(map(int,input().split()))
    n=m[s-1]
    n[(x-1)*3+y-1]=1
    if [1,1,1] in [n[0:3],n[3:6],n[6:],n[::3],n[1::3],n[2::3],n[::4],n[2:8:2]]:
        r=s
        break
    s=3-s
print(r)
