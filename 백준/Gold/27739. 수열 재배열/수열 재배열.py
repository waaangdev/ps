import copy
import bisect

a,b = map(int,input().split())
li = list(map(int,input().split()))
li2 = [[0] for i in range(a-b+1)]

for i in range(a-b+1):
    li2[i] = sorted(list(set(li[i:i+b])))
    #print(li2[i])

r = 0

for i in range(a-b+1):
    duml = 0
    if(i == 1):
        duml = 1
    elif(i > 1):
        duml = 1
        dum = li[i-1]
        for j in range(i-2,-1,-1):
            if(li[j] < dum):
                duml += 1
                dum = li[j]
            else:
                break
    dumr = 0
    if(i+b+1 == a):
        dumr = 1
    elif(i+b+1 < a):
        dumr = 1
        dum = li[i+b]
        for j in range(i+b+1,a):
            if(li[j] > dum):
                dumr += 1
                dum = li[j]
            else:
                break
    #print(duml,dumr)
    if(len(li2[i]) == b):
        dum = 1
        if(i+b+1 <= a):
            if(li2[i][b-1] >= li[i+b]):
                dum = 0
        if(i > 0):
            if(li[i-1] >= li2[i][0]):
                dum = 0
        if(dum):
            r = max(r,duml+dumr+b)
    #print(dumr)
    if(i > 0):
        for j in li2[i]:
            if(j > li[i-1]):
                duml+=1
    if(i+b+1 <= a):
        for j in li2[i]:
            if(j < li[i+b]):
                dumr+=1
    
    r = max(r,max([duml,dumr,len(li2[i])]))
    #print(i,r,duml,dumr)

print(r)
