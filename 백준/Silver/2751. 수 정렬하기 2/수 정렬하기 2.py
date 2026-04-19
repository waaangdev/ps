import sys
a = int(input())
l= []
for i in range(a):
    l.append(int(sys.stdin.readline()))
l = sorted(l)
for i in range(a):
    print(l[i])