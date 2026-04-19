a = int(input())
al = list(map(int,input().split()))
li1 = []
d = 0
d1 = 0
r = []
for i in range(a):
    '''
    if(al[i] > d):
        d1 += 1
    else:
        d1 = 1
    '''
    d =al[i]
    
    
    if(len(li1) == 0):
        d1 = 0
    else:
        sort1 = -1
        sort2 = len(li1)
        while 1:
            if(li1[(sort1+sort2)//2] < d):
                sort1 = (sort1+sort2)//2
            elif(li1[(sort1+sort2)//2] > d):
                sort2 = (sort1+sort2)//2
            else:
                d1 = (sort1+sort2)//2+1
                break
            if(abs(sort1 - sort2) < 2):
                d1 = (sort1+sort2)//2+1
                break
            
    if(len(li1) == 0):
        li1.append(d)
        r.append(len(li1))
    elif(len(li1)-1 < d1):
        if(d != li1[len(li1)-1]):
            li1.append(d)
            r.append(len(li1))
        else:
            r.append(d1)
    else:
        if(li1[d1] > d):
            if(d1 == 0):
                li1[d1] = d
                r.append(d1+1)
            elif(d != li1[d1-1]):
                li1[d1] = d
                r.append(d1+1)
            else:
                r.append(d1)
        else:
            r.append(d1)
            

rr = []
rr1 = len(li1)+1
for i in range(a):
    if(rr1-1 == r[len(r)-i-1]):
        rr.append(al[len(r)-i-1])
        rr1 -=1
    if(rr1 == 1):
        break
print(len(li1))
rr = reversed(rr)
print(*rr)