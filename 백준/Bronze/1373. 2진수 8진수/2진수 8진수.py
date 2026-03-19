a=input()
a=(3-len(a)%3)*'0'+a
r=[0]*(len(a)//3)
for i in range(len(a)-1,-1,-3):
    r[i//3]=int(a[i-2:i+1],2)
r = list(map(str,r))
for i in range(len(r)-1):
    if(r[i]=='0'):
        r[i]=''
    else:
        break
print(''.join(r))