
a,b,c = map(int,input().split())

d = max(c,a)

if(b < c):
    print("Bus")
elif(b > c):
    print("Subway")
else:
    print("Anything")