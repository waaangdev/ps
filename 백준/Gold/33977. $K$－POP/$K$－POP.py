#k-pop
n = int(input())
li = []
for i in range(1,n+1):
    if(n%i == 0):
        li.append(i)
d1,d2 = 0,0
if(len(li)%2 == 1):
    d1 = li[len(li)//2]
    d2 = d1
else:
    d2 = li[len(li)//2-1]
    d1 = li[len(li)//2]
print(d1+d2)
for i in range(d1-1):
    print(i+1,i+2)
for i in range(d2):
    print(d1-i,d1+i+1)