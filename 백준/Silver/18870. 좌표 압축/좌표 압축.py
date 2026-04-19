import sys
a = int(input())
li = list(map(int,sys.stdin.readline().strip().split()))
li2 = sorted(li)
li3 = {}
b = 0
for i in range(a):
    if(not li2[i] in li3):
        li3[li2[i]] = b
        b+=1
for i in li:
    print(li3[i],end = ' ')