li=input().split()
li.sort()
d=1
r=0
for i in range(4):
    if(li[i][0]==li[i+1][0]):
        d+=1
    else:
        d=1
    r=max(r,d)
print(r)