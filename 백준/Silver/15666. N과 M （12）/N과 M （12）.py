import sys
a,b = map(int,input().split())
alpa = sorted(list(map(int,sys.stdin.readline().strip().split())))
#alpa = sorted(input().split())
li = [1 for i in range(b)]
li[b-1] = 0 
llii2 = []
ii = 1
while ii != len(alpa):
    if(alpa[ii] == alpa[ii-1]):
        del alpa[ii]
        a-=1
        ii-=1
    ii+=1
while 1:
    c = 0
    li[b-1] += 1   
    for i in range(b-1,-1,-1):
        if(li[i] == a+1 and i != 0):
            li[i-1] += 1
            li[i] = 1
        if(c == 0 and i != b-1):
            if(li[i] > li[i+1]):
                c = 1
    if(li[0] > a):
        break
    if(c == 0):      
        llii = []
        for i in range(len(li)):
            llii.append(alpa[li[i]-1])
        llii2.append([llii[i] for i in range(len(llii))])
            
llii2 = sorted(llii2)
i = 1
while i != len(llii2):
    if(llii2[i] == llii2[i-1]):
        del llii2[i]
        i-=1
    i+=1
for i in llii2:
    print(*i)