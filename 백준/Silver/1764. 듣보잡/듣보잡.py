import sys
a,b= list(map(int,input().split()))
li1 = []
li2 = []
li3 = []
for i in range(a):
    li1.append(sys.stdin.readline())
for i in range(b):
    li2.append(sys.stdin.readline())
li3 = sorted(list(set(li1).intersection(li2)))
print(len(li3))
for i in li3:
    print(i,end = '')