import sys
a = int(input())
c = [0 for i in range(20)]
for i in range(a):
    b = sys.stdin.readline().split()
    if(len(b) == 2):b[1] = int(b[1])
    if(b[0] == 'add'):
        c[b[1]-1] +=1
    if(b[0] == 'remove'):
        if c[b[1]-1] != 0:c[b[1]-1] -=1
    if(b[0] == 'toggle'):
        if c[b[1]-1] != 0:c[b[1]-1] -=1
        else :c[b[1]-1] +=1
    if(b[0] == 'check'):
        if c[b[1]-1] != 0:print(1) 
        else :print(0) 
    if(b[0] == 'all'):
        c = [1 for i in range(20)]
    if(b[0] == 'empty'):
        c = [0 for i in range(20)]