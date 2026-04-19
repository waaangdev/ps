import math

a= int(input())
for i in range(a):
    b,c = map(int,input().split())
    d = c-b
    
    e = math.sqrt(d)
    if(e%1==0):
        print((int(e)-1)*2+1)
    else:
        if(int(e)**2+(int(e)+1)**2)/2 > d:
            print((int(e)-1)*2+2)
        else:
            print((int(e)-1)*2+3)