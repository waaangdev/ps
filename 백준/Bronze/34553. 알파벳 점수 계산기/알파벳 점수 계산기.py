a=input()
b=1
c=1
for i in range(1,len(a)):
    if(ord(a[i])>ord(a[i-1])):
        c+=1
    else:
        c=1
    b+=c
print(b)