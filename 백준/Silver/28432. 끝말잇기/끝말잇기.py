import sys

a1 = int(sys.stdin.readline())
li = []
b = 0
for i in range(a1):
    a = sys.stdin.readline().strip()
    li.append(a)
    if(a == "?"):
        b = i
if(a1 == 1):
    sys.stdin.readline().strip()
    print(sys.stdin.readline().strip())
elif(b == 0):
    c = li[b+1][0]
    a = int(sys.stdin.readline())
    li = set(li)
    for i in range(a):
        a = sys.stdin.readline().strip()
        if(a[-1] == c and (a not in li)):
            print(a)
            break
elif(b == a1-1):
    c = li[b-1][-1]
    a = int(sys.stdin.readline())
    li = set(li)
    for i in range(a):
        a = sys.stdin.readline().strip()
        if(a[0] == c and (a not in li)):
            print(a)
            break
else:
    c = li[b-1][-1]
    d = li[b+1][0]
    a = int(sys.stdin.readline())
    li = set(li)
    for i in range(a):
        a = sys.stdin.readline().strip()
        if(a[0] == c and a[-1] == d and (a not in li)):
            print(a)
            break