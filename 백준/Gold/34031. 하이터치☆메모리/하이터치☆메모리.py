a = input()
b = input()
li = [0]*(len(a)+1)
c =0
for i in range(len(a)):
    if(a[i]=='('):
        c+=1
    else:
        c-=1
    if(c>=0):
        li[c]+=1
    else:
        break
r = 0
c =0
d = 0
for i in range(len(b)):
    if(b[i]==')'):
        c+=1
        if(d!=0):d -= 1
    else:
        d += 1
        c-=1
    if(d==0 and c >=0 and c <= len(a)):
        r+=li[c]
print(r)