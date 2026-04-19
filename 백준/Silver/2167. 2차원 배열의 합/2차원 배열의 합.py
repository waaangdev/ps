import sys
a,b= map(int,input().split())
m = []
for i in range(a):
    m.append(list(map(int,sys.stdin.readline().split())))
c = int(input())
for i in range(c):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    s = 0
    for j in range(x1-1,x2):
        for k in range(y1-1,y2):
            s+=m[j][k]
    print(s)