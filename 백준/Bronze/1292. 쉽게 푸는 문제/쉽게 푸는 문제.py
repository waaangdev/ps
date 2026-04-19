a,b = map(int,input().split())
dum = []
for i in range(1,100):
    dum+=[i]*i
r =0
for i in range(a-1,b):
    r+=int(dum[i])
print(r)