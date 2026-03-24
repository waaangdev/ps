a=input()
pl=[1]
c=0
n=50000
li2 = [1]*n

for i in range(2,n):
    if(li2[i]):
        pl.append(i)
        
        for j in range(i*i,n,i):
            li2[j]=0
for i in a:
    if(ord(i) < ord("a")):
        c+=ord(i)-ord("A")+27
    else:
        c+=ord(i)-ord("a")+1
print("It is "+"not "*(c not in pl)+"a prime word.")