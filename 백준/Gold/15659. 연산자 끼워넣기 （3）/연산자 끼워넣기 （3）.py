import sys
from collections import deque

n = int(input())
li1 = list(map(int,input().split()))
li2 = list(map(int,input().split()))

def sol(li2,sums,priv,idx):
    if(idx == n):
        return [sums+priv,sums+priv]
    mins,maxs = 0,0
    init=0
    for i in range(4):
        if(li2[i] > 0):
            li22 = li2[:]
            li22[i] -= 1

            dum = 0
            if(i < 2):
                dum = sol(li22,sums+priv,li1[idx]*(1-i*2),idx+1)
            elif(i==2):
                dum = sol(li22,sums,priv*li1[idx],idx+1)
            elif(i==3):
                dum = sol(li22,sums,(abs(priv)//li1[idx])*(1-2*(priv<0)),idx+1)

          
            
            if(init==0):
                init=1
                mins = dum[0]
                maxs = dum[1]
            else:
                mins = min(mins,dum[0])
                maxs = max(maxs,dum[1])
    return [mins,maxs]

print('\n'.join(map(str,sol(li2[:],0,li1[0],1)[::-1])))