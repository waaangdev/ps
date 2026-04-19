a=list(map(int,input().split()))
b=1
c=0
for I in a:
    if I %2==1:
        b*= I 
        c=1
if(c==0):
    for I in a: b*= I 
print(b)