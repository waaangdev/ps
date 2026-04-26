def ccw(p11,p12,p21,p22,p31,p32):
    return (p21 - p11) * (p32 - p12) - (p31 - p11) * (p22 - p12);
a,b = map(int,input().split())
a1,b1 = map(int,input().split())
a2,b2 = map(int,input().split())
if(ccw(a,b,a1,b1,a2,b2)==0):
    print(ccw(a,b,a1,b1,a2,b2))
else:
    print(ccw(a,b,a1,b1,a2,b2)//abs(ccw(a,b,a1,b1,a2,b2)))