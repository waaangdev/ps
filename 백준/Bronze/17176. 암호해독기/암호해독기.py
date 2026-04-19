
import sys
from collections import deque

a = int(sys.stdin.readline())

li = [0 for i in range(53)]

li1 = list(map(int,sys.stdin.readline().split()))
c = 0

for i in range(a):
    if(li[li1[i]] == 0):
        c+=1
    li[li1[i]]+=1


li2 = sys.stdin.readline().strip()
r = 'y'

for i in range(a):
    ind = 0
    if(li2[i] != " "):
        if(ord(li2[i]) >= ord('a')):
            ind = ord(li2[i]) - ord('a')+27
        else:
            ind = ord(li2[i]) - ord('A')+1
    
    if(li[ind] == 0):
        r = 'n'
    li[ind] -=1
    if(li[ind] == 0):
        c-=1
if(c!=0):
    r = 'n'
print(r)
