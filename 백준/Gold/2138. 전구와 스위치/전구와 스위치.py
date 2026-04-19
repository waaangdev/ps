import sys

n = int(input())

a = sys.stdin.readline().strip()

b = sys.stdin.readline().strip()

li = [0]*n

for i in range(n):

    if(a[i]!=b[i]):

        li[i] = 1

def gmin(a,b):

    if(a<0):return b

    if(b<0):return a

    return min(a,b)

def sol(l,r):

    if(l+1==r):

        if(li[l]):

            return [[[[-1,-1],[-1,1]],[[0,-1],[-1,-1]]],[[[0,-1],[-1,-1]],[[-1,-1],[-1,1]]]]

        else:

            return [[[[0,-1],[-1,-1]],[[-1,-1],[-1,1]]],[[[-1,-1],[-1,1]],[[0,-1],[-1,-1]]]]

    

    mid= (l+r)//2

    ls = sol(l,mid)

    rs = sol(mid,r)

    rr = [[[[-1 for _ in range(2)]for _ in range(2)]for _ in range(2)]for _ in range(2)]

    for i in range(4):

        ili = [[0,0],[1,0],[0,1],[1,1]]

        ilii = ili[i]

        for j in [[0,0],[1,0],[0,1],[1,1]]:

            for k in [[0,0],[1,0],[0,1],[1,1]]:

                if(ls[ilii[0]][k[0]][j[0]][k[1]]> -1 and rs[k[1]][ilii[1]][k[0]][j[1]]>-1):

                    rr[ilii[0]][ilii[1]][j[0]][j[1]] = gmin(rr[ilii[0]][ilii[1]][j[0]][j[1]], ls[ilii[0]][k[0]][j[0]][k[1]]+rs[k[1]][ilii[1]][k[0]][j[1]])

    #print(l,r,rr)

    return rr

rrs = sol(0,n)

rrr = -1

for k in [[0,0],[1,0],[0,1],[1,1]]:

    rrr = gmin(rrr,rrs[0][0][k[0]][k[1]])

print(rrr)

