n = int(input())
li = []
def sol(n,x,l,h):
    global li
    if(n==0):
        d = ['']*sum(l)
        for i in range(len(l)):
            d[l[i]-1] = chr(ord('A')+i)
            l[i]-=1
        x = 0
        for i in range(len(d)):
            if(d[i]==''):
                if(l[x]==0):
                    x+=1
                d[i] = chr(ord('A')+x)
                l[x]-=1
        li.append(''.join(d))
    for i in range(x+1,min(n+1,h+2)):
        sol(n-i,i,l+[i],h+i)
sol(n,0,[],0)
if(li):
    print(sorted(li)[0])
else:
    print(-1)