import math
a,b=map(int,input().split())

def segche(l,r,maxr):#세그체~ l부터 r-1까지 루트(maxr) 이상의 소수를 제외한 소인수분해
    li = [0]*(50000+1)#소수
    li2 = [0]*(50000+1)#제곱수
    li22 = [0]*(50000+1)
    rli = [[] for i in range(r-l)]
    for i in range(2,len(li)):
        if(li[i]==0):
            st = i+i
            for j in range(st,len(li),i):
                li[j]=1
                if(li22[j]!=0 and li22[j]!=i):li2[j] = 1
                li22[j] = i
            i2 = 1
            for k in range(50):
                i2*=i
                if(i2 >= r):break
                st = max(i2,((l-1)//i2+1)*i2)
                for j in range(st,r,i2):
                    rli[j-l].append(i)
    return rli 
def sol(a):
    if(a==1):
        return 1
    li = segche(a,a+1,1000000000)[0]
    dum = 1
    for j in range(len(li)):
        dum*=li[j]
    if(dum!=a):
        #if(dum!=1):print(1,li[i-l],i)
        li.append(a)
    li.sort()
    li2 = []
    dum = li[0]
    dum2 = 0
    for j in range(len(li)):
        if(li[j]!=dum):
            li2.append(dum2)
            dum2 = 0
            dum=li[j]
        dum2+=1
    li2.append(dum2)
    rr =1
    for j in range(len(li2)):
        rr*=li2[j]+1
    #print(li,li2)
    return rr
#print(sol(b))
if(b%a==0):
    print(sol(b//a))
else:
    print(0)