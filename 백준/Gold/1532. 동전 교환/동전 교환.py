import math
li = list(map(int,input().split()))
li2 = list(map(int,input().split()))
li3 = [li[i]-li2[i] for i in range(3)]
#print(li3)
r = 0
if(li3[2]<0):
    r += math.ceil(-li3[2]/9)
    li3[1]-=math.ceil(-li3[2]/9)
    li3[2]+=math.ceil(-li3[2]/9)*9
if(li3[0]<0):
    r+=-li3[0]
    li3[1]-=-li3[0]*11
    li3[0]=0

if(li3[1]<0):
    if(li3[0]>0):
        dum=min(math.ceil(-li3[1]/9),li3[0])
        r += dum
        li3[0]-=dum
        li3[1]+=dum*9

if(li3[1]<0):
    if(li3[2]>0):
        dum=min(-li3[1]*11,li3[2]//11*11)
        r += dum//11
        li3[2]-=dum
        li3[1]+=dum//11

if(sorted([(i<0) for i in li3])[2]):
    print(-1)
else:
    print(r)