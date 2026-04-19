a = [1 for i in range(123457*2)]
b = 123457*2
for i in range(2,b):
    for j in range(i*i,123457*2,i):
        a[j]=0
a[0]=0
a[1]=0
a2=[0 for i in range(123457*2)]
a22=0
for i in range(123457*2):
    a22+=a[i]
    a2[i]=a22
while 1:
    f = int(input())
    if(f==0):break
    print(a2[f*2]-a2[f])