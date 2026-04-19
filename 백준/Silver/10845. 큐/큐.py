import sys
a = int(input())
c = []
for i in range(a):
    b = sys.stdin.readline().split()
    if(len(b) == 2):b[1] = int(b[1])
    if(b[0] == 'push'):
        c.append(b[1])
    if(b[0] == 'pop'):
        if len(c) != 0:print(c.pop(0))
        else: print(-1)
    if(b[0] == 'size'):
        print(len(c))
    if(b[0] == 'front'):
        if len(c) != 0:print(c[0])
        else: print(-1)
    if(b[0] == 'back'):
        if len(c) != 0:print(c[len(c)-1])
        else: print(-1)
    if(b[0] == 'empty'):
        if len(c) != 0:print(0)
        else: print(1)