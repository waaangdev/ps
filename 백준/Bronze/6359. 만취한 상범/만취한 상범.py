import sys
a = int(sys.stdin.readline())
for i in range(a):
    b = int(sys.stdin.readline())
    li = [1]*b
    for j in range(2,b+1):
        for k in range(len(li)):
            if((k+1)%j == 0):
                li[k] = li[k]*-1+1
    s = 0
    for k in range(len(li)):
        s+=li[k]
    print(s)