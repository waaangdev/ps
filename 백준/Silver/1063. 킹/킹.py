import sys
def move(m):
    mm = {'R':[0,1],'L':[0,-1],'B':[1,0],'T':[-1,0]}
    if(len(m) == 1):
        return mm[m]
    if(len(m) == 2):
        a = mm[m[0]]
        b = mm[m[1]]
        return [a[0]+b[0],a[1]+b[1]]
        
a,b,c= input().split()
ja = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
ja2 = ['A','B','C','D','E','F','G','H']
k = [8-int(a[1]),ja[a[0]]]
r = [8-int(b[1]),ja[b[0]]]

for i in range(int(c)):
    inp = input()
    k12 = list(k)
    r12 = list(r)
    m1 = move(inp)
    k[0] += m1[0]
    k[1] += m1[1]
    if(k == r):
        r[0] += m1[0]
        r[1] += m1[1]
    for i in range(2):
        if(k[i] < 0 or r[i] < 0 or k[i] > 7 or r[i] > 7):
            k = k12
            r = r12
            break

print(ja2[k[1]]+str(8-k[0]))
print(ja2[r[1]]+str(8-r[0]))
