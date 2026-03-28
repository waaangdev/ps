k,c = map(int,input().split())
k = str(k)

jubmi=0
for i in range(1,len(k)):
    if(k[:i]==k[-i:]):jubmi =i
r = 0

def sol(k,jub):
    return int(k)*len(k)-(int(k)-1)*jub

jubl = sol(k,jubmi)

for i in range(1,len(k)):
    dumk = (k[:i]*12)[:len(k)]
    nono=0
    if(int(dumk) < int(k)):
        if(dumk[i-1] != '9'):
            dumk = dumk[:i-1]+str(int(dumk[i-1])+1)
            dumk = (dumk[:i]*12)[:len(k)]
        else:
            nono=1
    if(not nono):
        #print(dumk)
        djubmi=0
        for i in range(1,len(dumk)):
            if(dumk[:i]==dumk[-i:]):djubmi =i

        r = max(r,jubl-sol(dumk,djubmi) - (int(dumk)-int(k))*c)
print(r)