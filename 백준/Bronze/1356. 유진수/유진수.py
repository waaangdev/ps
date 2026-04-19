a=input()
r=0
for i in range(1,len(a)):
    d=1
    for k in a[:i]:
        d*=int(k)
    s=1
    for k in a[i:]:
        s*=int(k)
    r=max(r,d==s)
print(["YES","NO"][1-r])
        