his=''
r =0
rr=0
input()
for i in input():
    if(i==his):r=0
    if(i in 'ha'):
        r+=1
        rr=max(rr,r)
    else:
        r=0
    his = i
print(rr)