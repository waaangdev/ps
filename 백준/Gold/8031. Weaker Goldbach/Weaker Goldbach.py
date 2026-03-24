li=[]
pl=[]
c=0
n=50000
li2 = [1]*n

for i in range(2,n):
    if(li2[i]):
        pl.append(i)
        
        for j in range(i*i,n,i):
            li2[j]=0


n2 = 2000000000
while (n2>5):
    i = n2//2
    li3=[1]*100
    for j in pl:
        for k in range(i//j*j,i+100,j):
            if(k>=i and k!=j):
                li3[k-i]=0
    for j in range(0,100):
        if(li3[j]):
            li.append(j+i)
    
    n2//=2
#print(li,pl[:20])


dp =[[] for i in range(10000)]
pl = pl[:100]
for i in pl:
    for j in pl:
        for k in pl:
            if(i!=j and j!=k and i!=k and (2 not in [i,j,k])):
                if(i+j+k<10000):
                    dp[i+j+k]=[i,j,k]
            
for i in pl:
    for j in pl:
        if(i!=j):
            if(i+j<10000 and (2 not in [i,j])):
                dp[i+j]=[i,j]
for _ in range(int(input())):
    n = int(input())
    n2 = n
    rl = []
    while 1:
        #print(n)
        for i in li:
            if(n//2<i<=n and n-i >= 10):
                n-=i
                rl.append(i)
                break
        if(n == 0):
            break
        if(n < 10000):
            if(dp[n] != []):
                rl+=dp[n]
                break
            if(li2[n]==1 and n!=2):
                rl.append(n)
                break
    if(len(set(rl))!=len(rl) or sum(rl)!=n2):print(0/0)
    #print(*sorted(rl))
    for i in rl:
        for j in pl:
            if(i%j==0 and i!=j):
                print(1/0)

    print(len(rl))
    print(*sorted(rl))
        