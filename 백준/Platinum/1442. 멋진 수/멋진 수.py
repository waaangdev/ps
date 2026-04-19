import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))
n,up,down=0,"",""

a,b = list(map(bin,map(int,sys.stdin.readline().split())))
down,up=(len(b)-len(a))*'0'+a[2:],b[2:]
n= len(up)
#print(down,up)
dps = [[[[[[-1 for i in range(2)] for i in range(2)] for i in range(2)] for i in range(3)] for i in range(3)] for i in range(n)]

def ddp(idx,ufit,dfit,zseq,oseq,notzero):
    if(zseq >= 3 or oseq >= 3):
        #print(idx,ufit,dfit,zseq,oseq,"=",(2**(n-idx)))
        if(ufit and dfit):
            return int("0b0"+up[idx:],2)+1-(int("0b0"+down[idx:],2))
        if(ufit):
            return int("0b0"+up[idx:],2)+1
        if(dfit):
            return (2**(n-idx))-(int("0b0"+down[idx:],2))
        return (2**(n-idx))
    if(idx == n):
        return 0
    
    if(dps[idx][zseq][oseq][ufit][dfit][notzero]!=-1):
        return dps[idx][zseq][oseq][ufit][dfit][notzero]

    st = 1
    ed = 0
    if(ufit):
        st = int(up[idx])
    if(dfit):
        ed = int(down[idx])

    r = 0
    for i in range(ed,st+1):
        r+=(ddp(idx+1,ufit and (st==i),dfit and (ed==i),(zseq+1)*(i==0)*notzero,(oseq+1)*(i==1),notzero or (i==1)))
    dps[idx][zseq][oseq][ufit][dfit][notzero] = r
    return r
print(ddp(0,1,1,0,0,0))
