a = int(input())

r1,r2 = 0,0
m = set([])

def qwe(aaa):
    asd = [aaa%i for i in range(2,aaa//2+1)]
    if(asd == []):
        asd = [1]
    return asd

if(a > 3 and a!= 5):
    a2 = sum([int(i) for i in str(a)])
    if(a2 %2 == 1):
        r1 = 1

a3 = qwe(a)#소수인지
a2 = a
if(a != 1):
    while(min(a3) == 0):
        a2 = round(a2 / (a3.index(0)+2))
        m.add(a3.index(0)+2)
        #print(a2,m)
        a3 = qwe(a2)
    m.add(a2)

if(a == 2 or a == 4 or (len(m) != 0 and len(m) % 2 == 0)):
    r2 = 1

#print(m)
if(r1):
    if(r2):
        print(4)
    else:
        print(1)
elif(r2):
    print(2)
else:
    print(3)

