import sys
a,b = map(int,input().split())
li = [[] for i in range(200)]
for i in range(a):
    c = sys.stdin.readline().strip().split()
    li[ord(c[0][0])].append([c[0],c[1]])
for i in range(b):
    c = sys.stdin.readline().strip()
    for j in range(len(li[ord(c[0])])):
        if(li[ord(c[0])][j][0] == c):
            print(li[ord(c[0])][j][1])
            break
            
    