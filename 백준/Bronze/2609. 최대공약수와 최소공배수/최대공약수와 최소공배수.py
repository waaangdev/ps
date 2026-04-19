import sys

b,c = map(int,sys.stdin.readline().split())
for i in range(min(b,c),0,-1):
    if(b%i == 0 and c%i==0):
        print(i)
        break
for i in range(min(b,c),b*c+1):
    if(i%b == 0 and i%c==0):
        print(i)
        break
    