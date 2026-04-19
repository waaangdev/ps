import sys
a,b = map(int,input().split())
l= []
s = 0
e = 0
for i in range(a):
    l.append(int(sys.stdin.readline()))
while 1:
    for i in range(e,len(l)):
        if(l[len(l)-i-1] <= b):
            s+=b//l[len(l)-i-1]
            b = b%l[len(l)-i-1]
            e = i
            break
    if(b == 0):
        break
print(s)