import sys
li = [[] for i in range(41)]
def p(n):
    global li 
    if(n == 0):
        return 1,0
    elif(n == 1):
        return 0,1
    elif(len(li[n]) != 0):
        return li[n];
    z,o = p(n-1)
    z1,o1 = p(n-2)
    z+=z1
    o+=o1
    li[n] = [z,o]
    return z,o;
a = int(input())
for _ in range(a):
    b = int(sys.stdin.readline().strip())
    s = p(b)
    print(s[0],s[1])