import sys
a,b=map(int,input().split())
li=[]
his = 0
for i in range(a):
    d = int(sys.stdin.readline())
    if(i==0):
        his = d
    else:
        li.append(d-his-1)
        his = d
r = sum(li)+a
#print(r)
li.sort(reverse=True)
for i in range(min(len(li),b-1)):
    r-=li[i]
print(r)