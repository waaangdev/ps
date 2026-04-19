n=int(input())
li=list(map(int,input().split()))
li.reverse()
mins = 100000000000000000
r=0
for i in li:
    mins=min(i,mins)
    r+=mins
print(r)