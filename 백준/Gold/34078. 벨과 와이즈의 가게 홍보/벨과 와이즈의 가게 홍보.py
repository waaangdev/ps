import sys
n = int(input())
li = list(map(int,sys.stdin.readline().strip().split()))

li2 = [0]*n
for i in range(n):
    li2[li[i]-1]=i

rr = n+1

for j in range(2):
    li3 = li[:]
    li22 = li2[:]
    r=0
    for i in range(n):
        dum = (n*j)+(1-j*2)*i+(1-j)
        #print(dum)
        if(li3[i]!=dum):
            r+=1
            li3[i],li3[li22[dum-1]] = li3[li22[dum-1]],li3[i]
            li22[li3[li22[dum-1]]-1] = li22[dum-1]
        #print(li3)
    rr = min(r,rr)

print(n-2,rr)

#10 9 8 7 6 4 3 5 2 1