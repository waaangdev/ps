import sys
a = int(input())
li = []
for i in range(500):
    if(i<3):
        li.append(1)
    else:
        li.append(li[i-2]+li[i-3])
for i in range(a):
    print(li[int(input())-1])