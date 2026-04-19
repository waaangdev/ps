import sys
from collections import deque#큐
from collections import Counter#최빈값
a = int(input())
li1 = list(map(int,input().split()))
li2 = list(map(int,input().split()))
li3 = list(map(int,input().split()))
s= []
for i in range(a-1,-1,-1):
    bl = []
    b =0
    if(not li1[i] in s):
        b+=1
        bl.append(li1[i])
    if(not li2[i] in s):
        b+=1
        bl.append(li2[i])
    if(not li3[i] in s):
        b+=1
        bl.append(li3[i])
    if(b == 3):
        if(li1[i]==li2[i] and li2[i]==li3[i]):
            s.insert(0, li1[i])
        elif(li1[i]==li2[i]):
            s.insert(0, li1[i])
            s.insert(0, li3[i])
        elif(li2[i]==li3[i]):
            s.insert(0, li2[i])
            s.insert(0, li1[i])
        elif(li1[i]==li3[i]):
            s.insert(0, li1[i])
            s.insert(0, li2[i])
    elif(b == 2):
        s.insert(0, bl[0])
    elif(b == 1):
        if(not li3[i] in s):
            s.insert(0, li3[i])
        elif(not li2[i] in s):
            s.insert(0, li2[i])
        elif(not li1[i] in s):
            s.insert(0, li1[i])
print(*s)